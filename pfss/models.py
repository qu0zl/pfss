from django.db import models
from django import forms
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
import re

# greg could be useful
#User.profile = property(lambda u: profiles.models.Profile.objects.get_or_create(user=u)[0])

MELEE=0
RANGED=1
SPECIAL=2

PRIMARY=0
SECONDARY=1
LIGHT=2
ONE_HANDED=3
TWO_HANDED=4

STR=1
DEX=2
CON=3
INT=4
WIS=5
CHA=6

FORT=1
REF=2
WILL=3

GOOD_SAVES={1:2, 2:3, 3:3, 4:4, 5:4, 6:5, 7:5, 8:6, 9:6, 10:7, 11:7, 12:8, 13:8, 14:9, 15:9, 16:10, 17:10, 18:11, 19:11, 20:12, 21:12, 22:13, 23:13, 24:14, 25:14, 26:15, 27:15, 28:16, 29:16, 30:17}
BAD_SAVES={1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2, 9:3, 10:3, 11:3, 12:4, 13:4, 14:4, 15:5, 16:5, 17:5, 18:6, 19:6, 20:6, 21:7, 22:7, 23:7, 24:8, 25:8, 26:8, 27:9, 28:9, 29:9, 30:10}
FAST_BAB={1:1, 2:2, 3:3, 4:5, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25, 26:26, 27:27, 28:28, 29:29, 30:30}
MEDIUM_BAB={1:0, 2:1, 3:2, 4:3, 5:3, 6:4, 7:5, 8:6, 9:6, 10:7, 11:8, 12:9, 13:9, 14:10, 15:11, 16:12, 17:12, 18:13, 19:14, 20:15, 21:15, 22:16, 23:17, 24:18, 25:18, 26:19, 27:20, 28:21, 29:21, 30:22}
SLOW_BAB={1:0, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5, 11:5, 12:6, 13:6, 14:7, 15:7, 16:8, 17:8, 18:9, 19:9, 20:10, 21:10, 22:11, 23:11, 24:12, 25:12, 26:13, 27:13, 28:14, 29:14, 30:15}


SAVES = ((FORT, 'Fortitude'), (REF, 'Reflex'), (WILL,'Will'))
STATS=((STR, 'Strength'), (DEX, 'Dexterity'), (CON, 'Constitution'), (INT,'Intelligence'), (WIS,'Wisdom'),(CHA,'Charisma'))

def formatNumber(number, noZero=False):
    if noZero and number == 0:
        return ''
    if ( number >= 0 ):
        return "+%s" % number
    else:
        return "%s" % number
class Die(models.Model):
    size = models.IntegerField()

    @property
    def half(self):
        return ((self.size/2)+0.5)

    def __unicode__(self):
        return u"d%s" % self.size

class Feat(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class GroupEntry(models.Model):
    Group = models.ForeignKey('CreatureGroup')
    creature = models.ForeignKey('Creature')
    text = models.CharField(max_length=128, blank=True)
    Augmented = models.BooleanField(default=False)
    def __unicode__(self):
        return "%s (%s)%s" % (self.Group, self.creature, self.text)

class CreatureGroup(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class CreatureType(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=128)
    BAB_Progression = models.IntegerField(default=2, choices=((1,'Slow'),(2,'Medium'),(3,'Fast')))
    GoodSave1 = models.IntegerField(default=None, choices=((None,'None'),)+SAVES, null=True, blank=True)
    GoodSave2 = models.IntegerField(default=None, choices=((None,'None'),)+SAVES, null=True, blank=True)
    GoodSave3 = models.IntegerField(default=None, choices=((None,'None'),)+SAVES, null=True, blank=True)
    def BAB(self, HD):
        if self.BAB_Progression == 1:
            return SLOW_BAB[HD]
        elif self.BAB_Progression == 2:
            return MEDIUM_BAB[HD]
        elif self.BAB_Progression == 3:
            return FAST_BAB[HD]
    def __unicode__(self):
        return self.name

class Language(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=128)
    stat = models.IntegerField(choices=STATS)
    def __unicode__(self):
        return self.name

class CreatureAttack(models.Model):
    class Meta:
        ordering = ['creature']
    attack = models.ForeignKey('Attack')
    creature = models.ForeignKey('Creature')
    extraText = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1)
    def __unicode__(self):
        if self.count > 1:
            return "%s (%s x %s)" % (self.creature, self.count, self.attack.__unicode__())
        return "%s (%s)" % (self.creature, self.attack.__unicode__())

class CreatureSkill(models.Model):
    class Meta:
        ordering = ['creature']
    extraText = models.TextField(null=True, blank=True)
    extraModifier = models.IntegerField(default=0)
    skill = models.ForeignKey('Skill')
    total = models.IntegerField(default=0)
    creature = models.ForeignKey('Creature')
    def __unicode__(self):
        return "%s (%s)" % (self.creature, self.skill)
    def modifiedTotal(self, creature=None):
        total = self.total
        if creature:
            if self.skill.stat == STR:
                total += (creature.Str-self.creature.Str)/2
            if self.skill.stat == DEX:
                total += (creature.Dex-self.creature.Dex)/2
            if self.skill.stat == CON:
                total += (creature.Con-self.creature.Con)/2
            if self.skill.stat == INT:
                total += (creature.Int-self.creature.Int)/2
            if self.skill.stat == WIS:
                total += (creature.Wis-self.creature.Wis)/2
            if self.skill.stat == CHA:
                total += (creature.Cha-self.creature.Cha)/2
        return total
    def renderSkill(self, creature=None):
        return "%s %s" % (self.skill, formatNumber(self.modifiedTotal(creature)))
    def getExtraText(self,creature=None):
        if self.extraText:
            returnText = self.extraText.replace('{{EXTRA_TOTAL}}', formatNumber(self.modifiedTotal(creature)+self.extraModifier))
            return " %s" % returnText
        else:
            return ""

    def render(self,creature=None):
        return "%s%s" % (self.renderSkill(creature), self.getExtraText(creature))


class Attack(models.Model):

    ATTACK_CLASSES=((PRIMARY, 'Primary'), (SECONDARY, 'Secondary'), (LIGHT, 'Light'), (ONE_HANDED,'One Handed'), ('TWO_HANDED','Two Handed'))
    ATTACK_TYPES=((MELEE, 'Melee'), (RANGED, 'Ranged'), (SPECIAL, 'SPECIAL'))
    name = models.CharField(max_length=64)
    dType = models.ForeignKey('Die', default=None)
    dCount = models.IntegerField(default=1)
    attackType = models.IntegerField(default=0, choices=ATTACK_TYPES)
    attackClass = models.IntegerField(default=0, choices=ATTACK_CLASSES)

    @property
    def dmg(self):
        return "%s%s" % (self.dCount, self.dType)
    def __unicode__(self):
        return u"%s %s%s" % (self.name, self.dCount, self.dType)

class SpecialAbility(models.Model):
    name = models.CharField(max_length=128)
    dynamicText = models.BooleanField(default=False)
    text = models.TextField()
    def __unicode__(self):
        return self.name
    def render(self, creature=None):
        if not self.dynamicText or not creature:
            return self.text
        else:
            returnText = self.text
            returnText = self.text.replace( '{{CHA_POS}}', creature.ChaText(True) )
            try:
                CON_MOD = int(returnText.split('{{CON_MOD_')[1].split('}')[0])
                CON_MOD += creature.ConMod
                returnText = re.sub('{{CON_MOD_[0-9]*?}}', str(CON_MOD), returnText)
            except IndexError:
                pass
            except Exception as e:
                import pdb; pdb.set_trace()
            returnText = returnText.replace( '{{HD}}', str(creature.HD) )
        return returnText

class Size(models.Model):
    name = models.CharField(max_length=64)
    ACbonus = models.IntegerField()
    reach = models.IntegerField()
    def __unicode__(self):
        return self.name

class Creature(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=256)
    Str = models.IntegerField()
    Dex = models.IntegerField()
    Con = models.IntegerField()
    Int = models.IntegerField()
    Wis = models.IntegerField()
    Cha = models.IntegerField()
    SR = models.IntegerField(default=0)
    #Speed = models.IntegerField(choices=map( lambda x: (x,str(x)), range(5,300,5)), default=30)
    Speed = models.CharField(max_length=256, blank=True)
    HDtype = models.ForeignKey('Die', default=None)
    Attacks = models.ManyToManyField('Attack', blank=True, null=True, through='CreatureAttack')
    Languages = models.ManyToManyField('Language', blank=True, null=True)
    Feats = models.ManyToManyField('Feat', blank=True, null=True)
    Groups = models.ManyToManyField('CreatureGroup', blank=True, null=True, through='GroupEntry')
    Size = models.ForeignKey('Size', default=None)
    Type = models.ForeignKey('CreatureType', default=None, null=True)
    Special = models.ManyToManyField('SpecialAbility', default=None, blank=True, null=True)
    HD = models.IntegerField(verbose_name='Hit-Dice', null=True) # Hit-dice
    armourAC = models.IntegerField(verbose_name='Armour Bonus', default=0)
    naturalAC = models.IntegerField(verbose_name='Natural AC Bonus', default=0)
    dodgeAC = models.IntegerField(verbose_name='Dodge AC Bonus', default=0)
    Skills = models.ManyToManyField('Skill', default=None, through='CreatureSkill', blank=True)
    Senses = models.CharField(max_length=256, blank=True)

    @property
    def BAB(self):
        return self.Type.BAB(self.HD) + self.Size.ACbonus
    @property
    def baseWillSave(self):
        return self.baseSave(WILL)
    @property
    def baseFortSave(self):
        return self.baseSave(FORT)
    @property
    def baseRefSave(self):
        return self.baseSave(REF)
    def baseSave(self, which):
        if which in (self.Type.GoodSave1, self.Type.GoodSave2, self.Type.GoodSave3):
            return GOOD_SAVES[self.HD]
        else:
            return BAD_SAVES[self.HD]

    def __unicode__(self):
        return u"%s" % (self.name)

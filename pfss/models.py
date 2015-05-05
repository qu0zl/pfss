from django.db import models
from django import forms
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User

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

class Die(models.Model):
    size = models.IntegerField()

    @property
    def half(self):
        return ((self.size/2)+0.5)

    def __unicode__(self):
        return u"d%s" % self.size

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
        return "%s %s%s" % (self.name, self.dCount, self.dType)

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
            returnText = returnText.replace( '{{HD}}', str(creature.HD) )
        return returnText

class Size(models.Model):
    name = models.CharField(max_length=64)
    ACbonus = models.IntegerField()
    reach = models.IntegerField()
    def __unicode__(self):
        return self.name

class Creature(models.Model):
    name = models.CharField(max_length=256)
    Str = models.IntegerField()
    Dex = models.IntegerField()
    Con = models.IntegerField()
    Int = models.IntegerField()
    Wis = models.IntegerField()
    Cha = models.IntegerField()
    BAB = models.IntegerField()
    Speed = models.IntegerField(choices=map( lambda x: (x,str(x)), range(5,300,5)), default=30)
    HDtype = models.ForeignKey('Die', default=None)
    Attacks = models.ManyToManyField('Attack')
    Size = models.ForeignKey('Size', default=None)
    Special = models.ManyToManyField('SpecialAbility', default=None)
    HD = models.IntegerField(verbose_name='Hit-Dice') # Hit-dice
    armourAC = models.IntegerField(verbose_name='Armour Bonus', default=0)
    naturalAC = models.IntegerField(verbose_name='Natural AC Bonus', default=0)
    dodgeAC = models.IntegerField(verbose_name='Dodge AC Bonus', default=0)

    def __unicode__(self):
        return u"%s" % (self.name)

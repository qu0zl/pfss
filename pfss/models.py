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
    HD = models.IntegerField(verbose_name='Hit-Dice') # Hit-dice
    armourAC = models.IntegerField(verbose_name='Armour Bonus', default=0)
    naturalAC = models.IntegerField(verbose_name='Natural AC Bonus', default=0)
    dodgeAC = models.IntegerField(verbose_name='Dodge AC Bonus', default=0)

    @property
    def HP(self):
        return int(((self.HDtype.half)+self.ConMod)*self.HD)
    @property
    def AC(self):
        return 10+self.DexMod+self.armourAC+self.Size.ACbonus+self.naturalAC+self.dodgeAC
    @property
    def touchAC(self):
        return 10+self.DexMod+self.Size.ACbonus+self.dodgeAC
    @property
    def flatFootedAC(self):
        return 10+self.Size.ACbonus+self.naturalAC+self.armourAC
    @property
    def ACcomponents(self):
        if self.armourAC or self.DexMod or self.naturalAC or self.dodgeAC or self.Size.ACbonus:
            return "(%s%s%s%s%s)" % ( \
                ("%s Arm " % self.armourAC) if self.armourAC else "", \
                ("%s Dex " % self.DexMod) if self.DexMod else "", \
                ("%s Nat " % self.naturalAC) if self.naturalAC else "", \
                ("%s Dge " % self.dodgeAC) if self.dodgeAC else "", \
                ("%s Sze " % self.Size.ACbonus) if self.Size.ACbonus else ""
                )
        else:
            return ''
    @property
    def melee(self):
        return self.Attacks.filter(attackType=MELEE)
    @property
    def meleeBonus(self):
        return self.BAB+self.StrMod
    def toHit(self,item):
        # TODO need to add weapon finesse feat support
        if item.attackType == MELEE:
            return "%s%s" % ( "+" if self.meleeBonus>=0 else "", self.meleeBonus)
        else:
            return 'Not yet implemented'


    @property
    def meleeText(self):
        first = True
        output=""
        for item in self.melee:
            if item.attackClass==TWO_HANDED or (self.melee.count()==1 and item.attackClass==PRIMARY):
                twoHandDmg=True
            else:
                twoHandDmg=False
            extraDmg = int(self.StrMod * (1 if twoHandDmg==False else 1.5))
            output = "%s%s%s %s %s%s%s" % (output,", " if not first else "",item.name, self.toHit(item), item.dmg, "+" if extraDmg>=0 else "", extraDmg)
            first=False
        return output

    @property
    def ranged(self):
        return self.Attacks.filter(attackType=RANGED)
    @property
    def special(self):
        return self.Attacks.filter(attackType=SPECIAL)
    @property
    def HPcomponents(self):
        return "(%s%s%s%s)" % (self.HD,self.HDtype,"+" if self.ConMod >= 0 else "", self.ConMod*self.HD)

    @property
    def initiative(self):
        return self.DexMod
    @property
    def Will(self):
        return "%s%s" % ("+" if self.WisMod >= 0 else "", self.WisMod)
    @property
    def Ref(self):
        return "%s%s" % ("+" if self.DexMod >= 0 else "", self.DexMod)
    @property
    def Fort(self):
        return "%s%s" % ("+" if self.ConMod >= 0 else "", self.ConMod)

    @property
    def StrMod(self):
        return (self.Str - 10)/2
    @property
    def DexMod(self):
        return (self.Dex - 10)/2
    @property
    def ConMod(self):
        return (self.Con - 10)/2
    @property
    def IntMod(self):
        return (self.Int - 10)/2
    @property
    def WisMod(self):
        return (self.Wis- 10)/2
    @property
    def ChaMod(self):
        return (self.Cha - 10)/2

    def __unicode__(self):
        return u"%s" % (self.name)

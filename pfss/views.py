from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.forms.models import modelformset_factory
import pfss.models

# Used to create an instance of a base creature and apply dynamic affects like
# augment summoning.
# The created instance is then passed to a template for rendering.
class creatureInstance(object):
    def __init__(self, base, augmentSummons=False):
        self.base = base
        self.augmented = augmentSummons
        for item in ("name","HD","Dex","Int","Wis","Cha","BAB","Speed","Size","armourAC","naturalAC"):
            try:
                setattr(self, item, base.__dict__[item])
            except Exception as e:
                print e
        self.Str = base.Str + 4 if augmentSummons else base.Str
        self.Con = base.Con + 4 if augmentSummons else base.Con
    @property
    def specials(self):
        specialsReturn = []
        for item in self.base.Special.all():
            specialsReturn.append(item.render(self))
        return specialsReturn
    @property
    def CMB(self):
        if (self.base.Size.ACbonus>=2): # Tiny or smaller
            statMod = self.DexMod
        else:
            statMod = self.StrMod
        return int(self.BAB+statMod-self.base.Size.ACbonus)
    @property
    def CMD(self):
        return int(10+self.BAB+self.StrMod+self.DexMod-self.base.Size.ACbonus) # TODO misc modifiers like 4 legs vs trip
    @property
    def HP(self):
        return int(((self.base.HDtype.half)+self.ConMod)*self.HD)
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
        return self.base.Attacks.filter(attackType=pfss.models.MELEE)
    @property
    def meleeBonus(self):
        return self.BAB+self.StrMod
    def toHit(self,item):
        # TODO need to add weapon finesse feat support
        if item.attackType == pfss.models.MELEE:
            return "%s%s" % ( "+" if self.meleeBonus>=0 else "", self.meleeBonus)
        else:
            return 'Not yet implemented'

    @property
    def meleeText(self):
        first = True
        output=""
        for item in self.melee:
            if item.attackClass==pfss.models.TWO_HANDED or (self.melee.count()==1 and item.attackClass==pfss.models.PRIMARY):
                twoHandDmg=True
            else:
                twoHandDmg=False
            extraDmg = int(self.StrMod * (1 if twoHandDmg==False else 1.5))
            output = "%s%s%s %s %s%s%s" % (output,", " if not first else "",item.name, self.toHit(item), item.dmg, "+" if extraDmg>=0 else "", extraDmg)
            first=False
        return output

    @property
    def ranged(self):
        return self.base.Attacks.filter(attackType=pfss.models.RANGED)
    @property
    def special(self):
        return self.base.Attacks.filter(attackType=pfss.models.SPECIAL)
    @property
    def HPcomponents(self):
        return "(%s%s%s%s)" % (self.HD,self.base.HDtype,"+" if self.ConMod >= 0 else "", self.ConMod*self.HD)
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
    def ChaText(self,ifPositive=False):
        charisma = self.ChaMod
        if (ifPositive and charisma < 0):
            charisma = 0
        return "%s%s" % ("+" if charisma >= 0 else "", charisma)

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

    def toHit(self,item):
        # TODO need to add weapon finesse feat support
        if item.attackType == pfss.models.MELEE:
            return "%s%s" % ( "+" if self.meleeBonus>=0 else "", self.meleeBonus)
        else:
            return 'Not yet implemented'




def creatureView(request, cid):

    creature = creatureInstance(pfss.models.Creature.objects.get(id=cid))

    return render_to_response('creature_view.html', \
        {
            'creature':creature,
        }, \
        RequestContext(request))


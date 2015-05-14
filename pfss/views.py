from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.forms.models import modelformset_factory
from pfss.models import formatNumber
import pfss.models

# Used to create an instance of a base creature and apply dynamic affects like
# augment summoning.
# The created instance is then passed to a template for rendering.
class creatureInstance(object):
    def __init__(self, base, augment=False, celestial=False, fiendish=False, entropic=False, resolute=False):
        self.base = base
        self.augmented = augment
        for item in ("name","HD","Dex","Int","Wis","Cha","BAB","Speed","Size"):
            try:
                setattr(self, item, base.__dict__[item])
            except Exception as e:
                print e
        self.Str = base.Str + 4 if augment else base.Str
        self.Con = base.Con + 4 if augment else base.Con
        self.BAB = base.BAB
        self.alignment = base.Alignment.short

        self.initExtraTypes(celestial, fiendish, entropic, resolute)
        self.initExtraTypesText()
        self.initSpecials()
    def initExtraTypes(self, celestial, fiendish, entropic, resolute):
        self.extraTypes = []
        self.extraTypes.extend(self.base.ExtraType.all())
        if celestial:
            self.extraTypes.append(pfss.models.CreatureExtraType.objects.get(name='Celestial'))
        elif fiendish:
            self.extraTypes.append(pfss.models.CreatureExtraType.objects.get(name='Fiendish'))
        elif entropic:
            self.extraTypes.append(pfss.models.CreatureExtraType.objects.get(name='Entropic'))
        elif resolute:
            self.extraTypes.append(pfss.models.CreatureExtraType.objects.get(name='Resolute'))
    def initSpecials(self):
        self.specialsReturn = []
        self.specialShort = ""
        first = True
        for item in self.base.Special.all():
            if item.text:
                self.specialsReturn.append({'name':item.name, 'text':item.render(self)})
            if item.isAttack:
                self.specialShort = "%s%s%s" % (self.specialShort, ", " if not first else "", item.name)
                first = False
        for extraType in self.extraTypes:
            for item in extraType.Special.all():
                if item.text:
                    self.specialsReturn.append({'name':item.name, 'text':item.render(self)})
                if item.isAttack:
                    self.specialShort = "%s%s%s" % (self.specialShort, ", " if not first else "", item.name)
                    first = False
    def initExtraTypesText(self):
        self.extraTypeDefencesText = ''
        self.extraSensesText =''
        for item in self.extraTypes:
            if item.Defense:
                self.extraTypeDefencesText = "%s%s " % (self.extraTypeDefencesText, item.RenderDefense(self))
            if item.Senses:
                self.extraSensesText = "%s%s " % (self.extraSensesText, item.Senses)
    @property
    def SR(self):
        # greg does this cause problems with base SR higher than would gain from template or
        # does that never actually occur?
        if True in map(lambda x: x.name=='Celestial' or x.name == 'Fiendish', self.extraTypes):
            return str(self.CRValue + 5)
    @property
    def CR(self): # needs to take CR increases from templates into account greg
        return self.base.CR()
    @property
    def CRValue(self): # needs to take CR increases from templates into account greg
        return self.base.CRValue()
    @property
    def extraTypesDefences(self):
        return self.extraTypeDefencesText

    @property
    def specials(self):
        return self.specialsReturn
    @property
    def Skills(self):
        skillsReturn = []
        for item in self.base.creatureskill_set.all():
            skillsReturn.append(item.render(self))
        return skillsReturn
    @property
    def perception(self):
        for item in self.Skills:
            if item.startswith('Perception'):
                return item
        return None
    @property
    def CMBValue(self):
        if (self.base.Size.ACbonus>=2): # Tiny or smaller
            statMod = self.DexMod
        else:
            statMod = self.StrMod
        return self.BAB+statMod-self.base.Size.ACbonus
    @property
    def BABtext(self):
        return formatNumber(self.BAB)
    @property
    def CMB(self):
        return formatNumber(self.CMBValue)
    @property
    def CMD(self):
        return int(10+self.BAB+self.StrMod+self.DexMod+self.dodgeAC-self.base.Size.ACbonus)
    @property
    def CMBText(self):
        return self.base.CMBTextRender(self.CMBValue)
    @property
    def CMDText(self):
        return self.base.CMDTextRender(self.CMD)
    @property
    def toughness(self):
        if self.base.Feats.filter(name='Toughness').count():
            if self.base.HD > 3:
                return self.base.HD
            else:
                return 3
        return 0
    @property
    def HP(self):
        return int(((self.base.HDtype.half)+self.ConMod)*self.HD)+self.toughness
    @property
    def AC(self):
        return 10+self.DexMod+self.base.armourAC+self.base.Size.ACbonus+self.base.naturalAC+(1 if self.base.Feats.filter(name='Dodge').count() else 0)
    @property
    def touchAC(self):
        return 10+self.DexMod+self.base.Size.ACbonus+self.dodgeAC
    @property
    def flatFootedAC(self):
        return 10+self.base.Size.ACbonus+self.base.naturalAC+self.base.armourAC + (self.DexMod if self.DexMod<0 else 0)
    @property
    def dodgeAC(self):
        return (1 if self.base.Feats.filter(name='Dodge').count() else 0)
    @property
    def ACcomponents(self):
        if self.base.armourAC or self.DexMod or self.base.naturalAC or self.dodgeAC or self.base.Size.ACbonus:
            return "(%s%s%s%s%s)" % ( \
                ("%s Arm " % self.base.armourAC) if self.base.armourAC else "", \
                ("%s Dex " % formatNumber(self.DexMod)) if self.DexMod else "", \
                ("%s Nat " % formatNumber(self.base.naturalAC)) if self.base.naturalAC else "", \
                ("+1 Dge " if self.dodgeAC else ""), \
                ("%s Sze " % formatNumber(self.base.Size.ACbonus)) if self.base.Size.ACbonus else ""
                )
        else:
            return ''
    @property
    def melee(self):
        return self.base.creatureattack_set.filter(attack__attackType=pfss.models.MELEE)
    @property
    def meleeBonus(self):
        mod = self.StrMod
        if self.base.Feats.filter(name='Weapon Finesse').count():
            if self.DexMod > mod:
                mod = self.DexMod
        return self.BAB+mod+self.base.Size.ACbonus
    @property
    def rangedBonus(self):
        mod = self.DexMod
        return self.BAB+mod+self.base.Size.ACbonus
    def toHit(self,item):
        if item.attackType == pfss.models.MELEE:
            if item.attackClass == pfss.models.SECONDARY and (self.melee.count() > 1 or (self.melee.count()==1 and self.melee.get().count>1)): 
                if self.base.Feats.filter(name='Multiattack').count():
                    return formatNumber(self.meleeBonus-2)
                else:
                    return formatNumber(self.meleeBonus-5)
            else:
                return formatNumber(self.meleeBonus)
        elif item.attackType == pfss.models.RANGED:
            return formatNumber(self.rangedBonus)
        else:
            return 'Not yet implemented'
    def renderAttack(self, existingText, first, item, extraDmg):
        attack = item.attack
        output = "%s%s%s%s %s (%s%s%s%s)" % (existingText,", " if (not first and not item.exclusive) else " or " if (not first and item.exclusive) else "", "%s x " % item.count if item.count > 1 else "", attack.name, self.toHit(attack), attack.dmg if item.attack.dCount else '', formatNumber(extraDmg, noZero=True) if item.attack.dCount else '', "/%s" % attack.crit if attack.crit else '', " %s" % item.extraText if item.extraText else '')
        return output
    @property
    def meleeText(self):
        first = True
        output=""
        for item in self.melee:
            attack = item.attack
            if self.StrMod < 0:
                dmgMultiplier = 1
            elif attack.attackClass==pfss.models.TWO_HANDED or ((self.melee.count()==1 and self.melee.get().count==1) and (attack.attackClass==pfss.models.PRIMARY or attack.attackClass==pfss.models.SECONDARY)):
                dmgMultiplier = 1.5
            elif attack.attackClass == pfss.models.SECONDARY:
                dmgMultiplier = 0.5
            else:
                dmgMultiplier = 1
            extraDmg = int(self.StrMod * dmgMultiplier)
            output = self.renderAttack(output, first, item, extraDmg)
            first=False
        return output

    @property
    def ranged(self):
        return self.base.creatureattack_set.filter(attack__attackType=pfss.models.RANGED)
    @property
    def rangedText(self):
        first = True
        output = ""
        for item in self.ranged:
            attack = item.attack
            if attack.rangedStrOption == pfss.models.ADD_STR or (attack.rangedStrOption == pfss.models.NEG_STR_ONLY and self.StrMod < 0):
                extraDmg = self.StrMod
            else:
                extraDmg = 0

            output = self.renderAttack(output, first, item, extraDmg)
            first = False
        return output
    #return self.base.creatureattack_set.filter(attack__attackType=pfss.models.RANGED)
    @property
    def special(self):
        return self.base.creatureattack_set.filter(attack__attackType=pfss.models.SPECIAL)
    @property
    def HPcomponents(self):
        return "(%s%s%s)" % (self.HD,self.base.HDtype, formatNumber((self.ConMod*self.HD)+self.toughness, noZero=True))
    @property
    def initiative(self):
        return self.DexMod + 4 if self.base.Feats.filter(name='Improved Initiative').count() else self.DexMod
    @property
    def initiativeText(self):
        return formatNumber(self.initiative)
    @property
    def Will(self):
        return formatNumber(self.WisMod+self.base.baseWillSave)
    @property
    def Ref(self):
        return formatNumber(self.DexMod+self.base.baseRefSave)
    @property
    def Fort(self):
        return formatNumber(self.ConMod+self.base.baseFortSave)
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

def creatureList(request, group_ID=None):
    creatures = pfss.models.Creature.objects.all()
    group = None
    extraTypes = []
    defaultTypes = []
    if group_ID:
        try:
            group = pfss.models.CreatureGroup.objects.get(id=group_ID)
            extraTypes = group.AllowedExtraType.all()
            defaultTypes = group.DefaultExtraType.all()
        except pfss.models.CreatureGroup.DoesNotExist:
            pass
        creatures = creatures.filter(Groups__id=group_ID)
        #creatureList = []
        #for creature in creatures:
        #    creatureList.append({'creature':creature, 'augmented':creature.groupentry_set.filter(Group_id=group_ID)[0].Augmented})
    else:
        extraTypes = pfss.models.CreatureExtraType.objects.all()

    return render_to_response('list.html', \
        {
            'group':group,
            'creatures':creatures,
            'extraTypes':extraTypes,
            'defaultTypes':defaultTypes,
        }, \
        RequestContext(request))

def handleList(request):
    creatures = []
    for key in request.POST:
        if key.startswith('creature_'):
            #if key.startswith('creature_augment_'):
            #    creature=creatureInstance(pfss.models.Creature.objects.get(id=int(key.split('_')[-1])), True)
            #else:
            id = int(key[9:])
            args = {}
            creature_prefix = 'modify_%s_' % id
            for inner in request.POST:
                if inner.startswith(creature_prefix):
                    argument = inner.split('_')[-1]
                    args[argument] = 1
            creature=creatureInstance(pfss.models.Creature.objects.get(id=id), **args)
            creatures.append(creature)
    return render_to_response('render.html', \
            {
                'creatures':creatures,
            }, \
            RequestContext(request))

def creatureView(request, cid):

    augment = bool(request.GET.get('augment'))
    celestial = bool(request.GET.get('celestial'))
    fiendish = bool(request.GET.get('infernal'))
    entropic = bool(request.GET.get('entropic'))
    resolute = bool(request.GET.get('resolute'))
    creature = creatureInstance(pfss.models.Creature.objects.get(id=cid), augment=augment, celestial=celestial, fiendish=fiendish, entropic=entropic, resolute=resolute)

    return render_to_response('creature_view.html', \
        {
            'creature':creature,
        }, \
        RequestContext(request))


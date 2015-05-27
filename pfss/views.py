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
    def __init__(self, base, augment=False, celestial=False, fiendish=False, entropic=False, resolute=False, noSpecials=False):
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
        self.initSpecials(noSpecials=noSpecials)
    def initExtraTypes(self, celestial, fiendish, entropic, resolute):
        self.extraTypes = []
        self.extraTypes.extend(self.base.ExtraType.all())
        def appendUnique(self, newType):
            if newType not in self.extraTypes:
                self.extraTypes.append(newType)
        if celestial:
            appendUnique(self, pfss.models.CreatureExtraType.objects.get(name='Celestial'))
        elif fiendish:
            appendUnique(self, pfss.models.CreatureExtraType.objects.get(name='Fiendish'))
        elif entropic:
            appendUnique(self, pfss.models.CreatureExtraType.objects.get(name='Entropic'))
        elif resolute:
            appendUnique(self, pfss.models.CreatureExtraType.objects.get(name='Resolute'))
    def initSpecials(self, noSpecials=False):
        self.specialsReturn = []
        self.specialShort = ""
        self.defenseShort = ""
        self.generalShort = ""
        self.statShort = ""
        first = True
        firstDefense = True
        firstGeneral = True
        firstStat = True
        for item in self.base.Special.all():
            if (not noSpecials) and item.text:
                self.specialsReturn.append({'name':item.name, 'text':item.render(self)})
            if item.isAttack:
                rs = item.renderShort(self) or item.name
                self.specialShort = "%s%s%s" % (self.specialShort, ", " if not first else "", rs)
                first = False
            elif item.isDefense:
                rs = item.renderShort(self) or item.name
                self.defenseShort = "%s%s%s" % (self.defenseShort, ", " if not firstDefense else "", rs)
                firstDefense = False
            elif item.isGeneral:
                rs = item.renderShort(self) or item.name
                self.generalShort = "%s%s%s" % (self.generalShort, ", " if not firstGeneral else "", rs)
                firstGeneral = False
            elif item.isStat:
                rs = item.renderShort(self) or item.name
                self.statShort = "%s%s%s" % (self.statShort, ", " if not firstStat else "", rs)
                firstStat = False
        for extraType in self.extraTypes:
            for item in extraType.Special.all():
                if (not noSpecials) and item.text:
                    self.specialsReturn.append({'name':item.name, 'text':item.render(self)})
                if item.isAttack:
                    rs = item.renderShort(self) or item.name
                    self.specialShort = "%s%s%s" % (self.specialShort, ", " if not first else "", rs)
                    first = False
                elif item.isDefense:
                    rs = item.renderShort(self) or item.name
                    self.defenseShort = "%s%s%s" % (self.defenseShort, ", " if not firstDefense else "", rs)
                    firstDefense = False
                elif item.isGeneral:
                    rs = item.renderShort(self) or item.name
                    self.generalShort = "%s%s%s" % (self.generalShort, ", " if not firstGeneral else "", rs)
                    firstGeneral = False
                elif item.isStat:
                    rs = item.renderShort(self) or item.name
                    self.statShort = "%s%s%s" % (self.statShort, ", " if not firstStat else "", rs)
                    firstStat = False

    def initExtraTypesText(self):
        DV_STRING='darkvision 60 ft.'
        self.extraTypeDefencesText = ''
        self.extraSensesText =''
        for item in self.extraTypes:
            if item.Defense:
                self.extraTypeDefencesText = "%s%s " % (self.extraTypeDefencesText, item.RenderDefense(self))
            if item.Senses:
                if self.base.Senses.find(DV_STRING) != -1 and item.Senses.find(DV_STRING) != -1:
                    self.extraSensesText = "%s%s " % (self.extraSensesText, item.Senses.replace(DV_STRING,''))
                else:
                    self.extraSensesText = "%s%s " % (self.extraSensesText, item.Senses)
    @property
    def SR(self):
        SRValue = 0 if not self.base.SR else int(self.base.SR)
        if True in map(lambda x: x.name in ('Celestial','Fiendish','Entropic','Resolute'), self.extraTypes):
            if (self.CRValue+5) > SRValue:
                SRValue = self.CRValue + 5
        return (str(SRValue) if SRValue else "")
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
        if (self.base.Size.ACbonus>=2) or self.base.Feats.filter(name='Agile Maneuvers').count(): # Tiny or smaller
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
        return 10+self.DexMod+self.base.armourAC+self.base.Size.ACbonus+self.base.naturalAC+self.base.deflectAC+self.base.shieldAC+(1 if self.base.Feats.filter(name='Dodge').count() else 0)
    @property
    def touchAC(self):
        return 10+self.DexMod+self.base.Size.ACbonus+self.dodgeAC+self.base.deflectAC
    @property
    def flatFootedAC(self):
        return 10+self.base.Size.ACbonus+self.base.naturalAC+self.base.deflectAC+self.base.shieldAC+self.base.armourAC + (self.DexMod if self.DexMod<0 else 0)
    @property
    def dodgeAC(self):
        return (1 if self.base.Feats.filter(name='Dodge').count() else 0)
    @property
    def ACcomponents(self):
        if self.base.armourAC or self.DexMod or self.base.naturalAC or self.base.deflectAC or self.base.shieldAC or self.dodgeAC or self.base.Size.ACbonus or self.base.extraACText:
            return "(%s%s%s%s%s%s%s%s)" % ( \
                ("%s Arm " % formatNumber(self.base.armourAC)) if self.base.armourAC else "", \
                ("%s Shd " % formatNumber(self.base.shieldAC)) if self.base.shieldAC else "", \
                ("%s deflection " % formatNumber(self.base.deflectAC)) if self.base.deflectAC else "", \
                ("%s Dex " % formatNumber(self.DexMod)) if self.DexMod else "", \
                ("%s Nat " % formatNumber(self.base.naturalAC)) if self.base.naturalAC else "", \
                ("+1 Dge " if self.dodgeAC else ""), \
                ("%s Sze " % formatNumber(self.base.Size.ACbonus)) if self.base.Size.ACbonus else "", \
                self.base.extraACText if self.base.extraACText else ''
                )
        else:
            return ''
    @property
    def melee(self):
        return self.base.creatureattack_set.filter(attack__attackType=pfss.models.MELEE)
    def meleeByExclusive(self, exclusive):
        return self.melee.filter(exclusive=exclusive)
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
    def toHit(self,creatureAttack):
        item = creatureAttack.attack
        weaponFocus = 1 if self.base.Feats.filter(name__startswith='Weapon Focus (%s)'%item.name).count() else 0
        weaponFocus += item.bonusToHit
        if item.attackType == pfss.models.MELEE:
            if (item.attackClass == pfss.models.SECONDARY or creatureAttack.makeSecondary) and (self.melee.count() > 1 or (self.melee.count()==1 and self.melee.get().count>1)): 
                if self.base.Feats.filter(name='Multiattack').count():
                    return formatNumber(self.meleeBonus-2+weaponFocus)
                else:
                    return formatNumber(self.meleeBonus-5+weaponFocus)
            else:
                returnText = "%s" % formatNumber(self.meleeBonus+weaponFocus)
                if creatureAttack.noIterative == False and item.attackClass in (pfss.models.LIGHT, pfss.models.ONE_HANDED, pfss.models.TWO_HANDED):
                    iterative = self.BAB - 5
                    while iterative > 0:
                        returnText= "%s/+%s" % (returnText, (self.meleeBonus+weaponFocus+(iterative-self.BAB)))
                        iterative -= 5
                    if creatureAttack.extraAttackAtFullBAB:
                        returnText = "+%s/%s" % (self.meleeBonus+weaponFocus,returnText)
                return returnText
        elif item.attackType == pfss.models.RANGED:
            if creatureAttack.extraAttackAtFullBAB and self.base.Feats.filter(name='Rapid Shot').count():
                rapidShot = -2
            else:
                rapidShot = 0
            returnText = "%s" % formatNumber(self.rangedBonus+weaponFocus+rapidShot)
            if creatureAttack.noIterative == False:
                iterative = self.BAB - 5
                while iterative > 0:
                    returnText= "%s/+%s" % (returnText, (self.rangedBonus+weaponFocus+rapidShot+(iterative-self.BAB)))
                    iterative -= 5
                if creatureAttack.extraAttackAtFullBAB:
                    returnText = "+%s/%s" % (self.rangedBonus+weaponFocus+rapidShot,returnText)
            return returnText
        else:
            return 'Not yet implemented'
    def renderAttack(self, existingText, first, item, extraDmg, exclusive=False):
        attack = item.attack
        output = "%s%s%s%s %s%s (%s%s%s%s)" % (existingText,", " if (not first and item.exclusive==exclusive) else " or " if (not first and item.exclusive != exclusive) else "", "%s x " % item.count if item.count > 1 else "", attack.name, self.toHit(item), ' touch' if item.touchAttack else '', attack.dmg if item.attack.dCount else '', formatNumber(extraDmg, noZero=True) if item.attack.dCount else '', "/%s" % attack.crit if attack.crit else '', "%s" % ("%s%s" %(' ' if item.attack.dCount else '', item.extraText)) if item.extraText else '')
        return output
    def meleeDmgBonus(self, item, AsSole=False):
        attack = item.attack
        if self.StrMod < 0:
            dmgMultiplier = 1
        elif AsSole or item.wield2Handed:
            dmgMultiplier = 1.5
        elif attack.attackClass==pfss.models.TWO_HANDED or ((self.meleeByExclusive(item.exclusive).count()==1 and self.meleeByExclusive(item.exclusive).get().count==1) and (attack.attackClass==pfss.models.PRIMARY or attack.attackClass==pfss.models.SECONDARY)):
            dmgMultiplier = 1.5
        elif attack.attackClass == pfss.models.SECONDARY or item.makeSecondary:
            dmgMultiplier = 0.5
        else:
            dmgMultiplier = 1
        return (int(self.StrMod * dmgMultiplier)+attack.bonusToDmg)
    @property
    def meleeText(self):
        first = True
        exclusive = False
        output=""
        for item in self.melee:
            extraDmg = self.meleeDmgBonus(item)
            output = self.renderAttack(output, first, item, extraDmg, exclusive)
            exclusive = item.exclusive
            first=False
        return output
    def firstMeleeAttackDmg(self, AsSole=False, baseOnly=False):
        try:
            item = self.melee[0]
            if baseOnly:
                return u'%s' % item.attack.dmg
            extraDmg = self.meleeDmgBonus(item, AsSole)
            return u'%s%s' % (item.attack.dmg , formatNumber(extraDmg, noZero=True))
        except IndexError:
            return '?x? +?'

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
            extraDmg += attack.bonusToDmg

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
    def MiscMod(self):
        miscMod = 0
        if self.base.Special.filter(name="Cat's Luck (Su)").count():
            miscMod = self.ChaMod if self.ChaMod > 0 else 0
        return miscMod
    @property
    def Will(self):
        return formatNumber(self.WisMod+self.base.baseWillSave+self.MiscMod)
    @property
    def Ref(self):
        return formatNumber(self.DexMod+self.base.baseRefSave+self.MiscMod)
    @property
    def Fort(self):
        return formatNumber(self.ConMod+self.base.baseFortSave+self.MiscMod)
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

def creatureListByCode(request, code):
    try:
        group = pfss.models.CreatureGroup.objects.filter(code=code)[0]
    except IndexError:
        return redirect('../../')
    return creatureList(request, group_ID=group.id)

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

    font_size = request.POST.get('font_size', '0.875em')
    columns = int(request.POST.get('columns', '2'))
    if columns == 1:
        width = "100%"
    elif columns == 2:
        width = "50%"
    elif columns == 3:
        width = "33.33%"
    elif columns == 4:
        width = "25%"
    else:
        width = str(100.0/columns)+"%"
        
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
                'font_size':font_size,
                'width':width
            }, \
            RequestContext(request))

def creatureView(request, cid):

    augment = bool(request.GET.get('augment'))
    celestial = bool(request.GET.get('celestial'))
    fiendish = bool(request.GET.get('infernal'))
    entropic = bool(request.GET.get('entropic'))
    resolute = bool(request.GET.get('resolute'))
    noSpecials = bool(request.GET.get('noSpecials'))
    creature = creatureInstance(pfss.models.Creature.objects.get(id=cid), augment=augment, celestial=celestial, fiendish=fiendish, entropic=entropic, resolute=resolute, noSpecials=noSpecials)

    return render_to_response('creature_view.html', \
        {
            'creature':creature,
        }, \
        RequestContext(request))


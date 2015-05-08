
from django.contrib import admin
from pfss.models import SpecialAbility, Size, Die, Creature, Attack, Skill, CreatureSkill, CreatureType, Feat, Language, CreatureAttack, CreatureGroup, GroupEntry

admin.site.register(Language)
admin.site.register(Feat)
admin.site.register(GroupEntry)
admin.site.register(CreatureGroup)
admin.site.register(CreatureAttack)
admin.site.register(CreatureType)
admin.site.register(CreatureSkill)
admin.site.register(Skill)
admin.site.register(Attack)
admin.site.register(SpecialAbility)
admin.site.register(Die)
admin.site.register(Size)
admin.site.register(Creature)



from django.contrib import admin
from pfss.models import SpecialAbility, Size, Die, Creature, Attack, Skill, CreatureSkill, CreatureType, Feat

admin.site.register(Feat)
admin.site.register(CreatureType)
admin.site.register(CreatureSkill)
admin.site.register(Skill)
admin.site.register(Attack)
admin.site.register(SpecialAbility)
admin.site.register(Die)
admin.site.register(Size)
admin.site.register(Creature)


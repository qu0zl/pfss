
from django.contrib import admin
from pfss.models import SpecialAbility, Size, Die, Creature, Attack

admin.site.register(Attack)
admin.site.register(SpecialAbility)
admin.site.register(Die)
admin.site.register(Size)
admin.site.register(Creature)


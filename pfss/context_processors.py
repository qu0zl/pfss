from pfss.models import CreatureGroup

def site_wide_context(request):
    return { 'groups': CreatureGroup.objects.all() }


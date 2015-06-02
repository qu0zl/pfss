from pfss.models import Grouping

def site_wide_context(request):
    return { 'groupings': Grouping.objects.all() }


from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.forms.models import modelformset_factory
import pfss.models


def creatureView(request, cid):

    creature = pfss.models.Creature.objects.get(id=cid)

    return render_to_response('creature_view.html', \
        {
            'creature':creature,
        }, \
        RequestContext(request))


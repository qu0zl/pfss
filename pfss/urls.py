from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from . import views

prefix=""
#prefix='pfs/' # used to run with runserver
urlpatterns = patterns(
    "",
    url(r"^%s$" % prefix, TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^%sadmin/" % prefix, include(admin.site.urls)),
    url(r"^%saccount/" % prefix, include("account.urls")),
    url(r'^%slist/handle/$' % prefix, views.handleList),
    url(r'^%slist/$' % prefix, views.creatureList),
    url(r'^%slist/(?P<group_ID>\d+)/$' % prefix, views.creatureList),
    url(r'^%screature/(\d+)/$' % prefix, views.creatureView),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

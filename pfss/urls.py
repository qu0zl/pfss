from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pfss import views as pfss_views

from django.contrib import admin

from . import views

prefix=""
#prefix='pfs/' # used to run with runserver
urlpatterns = [
    url(r"^%s$" % prefix, TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^%sadmin/" % prefix, include(admin.site.urls)),
    url(r"^%saccount/" % prefix, include("account.urls")),
    url(r'^%slist/handle/$' % prefix, pfss_views.handleList),
    url(r'^%slist/$' % prefix, pfss_views.creatureList),
    url(r'^%slist/(?P<group_ID>\d+)/$' % prefix, pfss_views.creatureList),
    url(r'^%slist/code/(?P<code>\w+)/$' % prefix, pfss_views.creatureListByCode),
    url(r'^%screature/(\d+)/$' % prefix, pfss_views.creatureView),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

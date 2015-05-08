from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from . import views

urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^list/handle/$', views.handleList),
    url(r'^list/$', views.creatureList),
    url(r'^list/(?P<group>\d+)/$', views.creatureList),
    url(r'^creature/(\d+)/$', views.creatureView),
    url(r'^creature/(\d+)/augment/$', views.creatureView, kwargs={"augmentSummons":True}),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

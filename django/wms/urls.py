from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^challenge/', include('challenge.urls', namespace='challenge')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, url

urlpatterns = patterns('challenge.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<challenge_id>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<challenge_id>\d+)/answer/$', 'answer', name='answer'),
    url(r'^(?P<challenge_id>\d+)/solved/$', 'solved', name='solved'),
)

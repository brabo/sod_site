from django.conf.urls import patterns, url

from sod import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^query/$', views.query, name='query'),
)

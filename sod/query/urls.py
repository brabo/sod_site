from django.conf.urls import patterns, url

from sod import views

urlpatterns = patterns('',
#    url(r'^$', views.query, name='index'),
    url(r'^$', views.query, name='query'),
)

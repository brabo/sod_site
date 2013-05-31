from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sod_site.views.home', name='home'),
    # url(r'^sod_site/', include('sod_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('sod.urls')),
    url(r'^stats/$', include('sod.stats.urls')),
    url(r'^query/$', include('sod.query.urls')),

#    url(r'^stats/', include('sod.stats.urls')),
#    url(r'^query/', include('sod.query.urls')),
)

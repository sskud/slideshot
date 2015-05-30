# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
import broadcasts
from django.contrib import admin
import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index),
    #url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^loginza/', include('loginza.urls')),
    url(r'^api', include('api.urls')),
    url(r'^', include('broadcasts.urls')),
    url(r'^', include('home.urls')),
    #url('^media/$', 'django.views.static.serve',
     #   {'document_root':'/var/home/hosting_leidenit/projects/slideshot/static'}),
    url(r'^users/', include('users.urls')),
)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
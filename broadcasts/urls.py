# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
from broadcasts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # примерные адреса:
    #    /channels/
    #    /channel/<id>
    #    /mychannel/
    #    /broadcast/<id>
    
    url(r'^mainpage/$', views.mainpage),#first public
    
    #url(r'^event/$', views.event_list),#first public
    url(r'^broadcasting/$', views.broadcasting_list),#first public
    
    url(r'^broadcasting/(?P<id>[0-9]+)/$', views.broadcasting),
    #url(r'^event/(?P<id>[0-9]+)/$', views.event),
   # url(r'^index/$', views.index),
)

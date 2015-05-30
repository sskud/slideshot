# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'slides', views.SlideViewSet)

urlpatterns = patterns('',
        #примерные адреса api
    #    get_slide/<br>/<pos>
    #    get_slide/<br>
    #    add_slide/
    #    
    url(r'^', include(router.urls)),
    
    #url(r'slide/(?P<bk>[0-9]+)/(?P<pos>[0-9]+)/$', views.Slide.as_view()),
    #url(r'slide_get/$', views.SlideGet.as_view()),
    url(r'slide/(?P<bk>[0-9]+)/(?P<pos>[0-9]+)/$', views.SlideDetail.as_view()),
    url(r'slide/(?P<bk>[0-9]+)/$', views.SlideList.as_view()),
    
    #upload slide
    url(r'slide/$', views.Slide.as_view()),
    
    #user id - временно - пока не будет авторизации
    url(r'broadcasting/(?P<user_id>[0-9]+)/$', views.BroadcastingView.as_view()),
    url(r'getBkId/(?P<user_id>[0-9]+)/$', views.CurrentBroadcasting.as_view()),
    url(r'getuserid/$', views.GetUserID.as_view()),

    
    #url(r'token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)

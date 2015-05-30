from django.conf.urls import *
from .views import complete_registration


urlpatterns = patterns('',
    url(r'^complete_registration/$', complete_registration, name='users_complete_registration'),
    url(r'^logout/$', 'users.views.logout', name='users_logout'),
)
# -*- coding: utf-8 -*- 
from django.contrib import admin
from broadcasts.models import Event, Broadcasting, Slide
# Register your models here.
admin.site.register(Event)
admin.site.register(Broadcasting)
admin.site.register(Slide)
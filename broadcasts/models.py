# -*- coding: utf-8 -*- 
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.crypto import get_random_string

from tags.models import Tag

def get_upload_path(instance, filename):
        return 'slides/images/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 
    
# model of Event (group of broadcastings which have something same)
class Event(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'Владелец', related_name=u'events')
    members = models.ManyToManyField(User, verbose_name=u'Участники', related_name=u'membership')
    subscribers =  models.ManyToManyField(User, verbose_name=u'Подписчики', related_name=u'subscription')
    title = models.CharField(u'Заголовок', max_length=200)
    desc = models.TextField(u'Описание', max_length = 10000)
    is_public = models.BooleanField(u'Is public event?', default=True)
    
    class Meta: 
        db_table = 'broadcasts_events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering=['title']
    
    def __unicode__(self):
        return self.title

# model of Broadcasting
class Broadcasting(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'Владелец', related_name=u'broadcasts')
    
    title = models.CharField(u'Заголовок', max_length=40)
    desc = models.TextField(u'Описание', max_length = 10000)
    
    start_date = models.DateTimeField(u'Дата и время начала',default=datetime.now, blank=True)
    active = models.BooleanField(u'Активна сейчас?', default=False)
    public = models.BooleanField(u'Is public broadcasting?', default=True)
    
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name='Событие', related_name=u'broadcasts', blank=True, null=True)#relation to event
    #???можно будет добавить количество просмотров презентации
    class Meta: 
        db_table = 'broadcasts_broadcastings'
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'
        ordering=['start_date']
    
    def __unicode__(self):
        #privacy added for debug
        if self.is_public:
            privacy = 'Public'
        else:
            privacy = 'Private'
        return self.title + '[' + privacy + ']'
    
    def is_public(self):
        if (event and event.is_public or not event):
            return public
        elif (event and not event.is_public):
            return False
        
# model of Slide
class Slide(models.Model):
    file = models.ImageField(upload_to=get_upload_path)
    broadcasting = models.ForeignKey(Broadcasting, related_name=u'slides', verbose_name=u'Презентация')
    position = models.IntegerField(u'Порядковый номер', default=-1)
    dt_upload = models.DateTimeField(u'Дата загрузки',auto_now_add=True) 
    dt_create = models.IntegerField(u'Дата создания')

    
    class Meta: 
        db_table = 'broadcasts_slides'
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering=['position']
    
    def __unicode__(self):
        return self.broadcasting.__unicode__()+" #"+self.position.__str__()
    
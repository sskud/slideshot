# -*- coding: utf-8 -*- 
from django.db import models

class Tag(models.Model):
    title = models.CharField(u'Название', max_length=40)
    
    class Meta():
        db_table = 'tags_tag'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering=['title']

    def __unicode__(self):
        return self.title
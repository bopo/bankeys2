# coding:utf-8
from __future__ import unicode_literals
from django.db import models

TYPE_CHOICES = ((1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad'))


class Video(models.Model):
    name = models.CharField(max_length=64)
    quality = models.SmallIntegerField(choices=TYPE_CHOICES, default=1)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % (self.name,)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = (u'视频')
        verbose_name_plural = (u'视频')

class Customer(models.Model):

    def __unicode__(self):
        return '%s' % (self.name,)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = (u'客服')
        verbose_name_plural = (u'客服')
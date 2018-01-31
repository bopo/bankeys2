# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from model_utils.models import TimeStampedModel
from pilkit.processors import ResizeToFill
from django.utils.translation import ugettext_lazy as _

from service.consumer.models import Contains


class Timeline(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='timeline')
    owner_contains = models.ForeignKey(Contains, related_name='owner_contains', blank=True, null=True, default='')

    content = models.CharField(verbose_name=_(u'内容'), blank=True, null=True, max_length=255, db_index=True)
    picurl = ProcessedImageField(verbose_name=_(u'缩略图'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', null=True, default='avatar/default.jpg')
    video = models.CharField(verbose_name=_(u'视频'), blank=True, null=True, max_length=255, db_index=True)

    def __unicode__(self):
        return self.owner

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'朋友圈')
        verbose_name_plural = _(u'朋友圈')


class Comment(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment')
    owner_time = models.ForeignKey(Timeline, related_name='owner_time', blank=True, null=True, default='')
    article_id = models.CharField(verbose_name=_(u'原文章ID'), max_length=10, blank=True, null=True)
    comment = models.CharField(verbose_name=_(u'评论内容'), blank=True, null=True, max_length=255, db_index=True)

    def __unicode__(self):
        return self.owner

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'评论')
        verbose_name_plural = _(u'评论')


class Reply(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reply')
    owner_comment = models.ForeignKey(Comment, related_name='owner_comment', blank=True, null=True, default='')
    article_id = models.CharField(verbose_name=_(u'原文章ID'), max_length=10, blank=True, null=True)
    comment = models.CharField(verbose_name=_(u'回复内容'), blank=True, null=True, max_length=255, db_index=True)
    finrind_id = models.CharField(verbose_name=_(u'回复对象ID'), max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.owner

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'回复')
        verbose_name_plural = _(u'回复')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from service.consumer.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    '''
    公告管理
    '''
    list_display = ('subject', 'content')

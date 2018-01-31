# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from service.kernel.models.video import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'quality', 'is_active')

    def has_add_permission(self, request):
        return False


admin.site.register(Video, VideoAdmin)

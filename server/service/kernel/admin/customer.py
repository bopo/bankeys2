# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from service.kernel.models.video import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

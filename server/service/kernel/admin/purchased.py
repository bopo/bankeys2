# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from service.trade.models import Purchased


@admin.register(Purchased)
class PurchasedAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from service.kernel.models.consumption import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from service.kernel.models.enterprise import EnterpriseUser


@admin.register(EnterpriseUser)
class EnterpriseUserAdmin(VersionAdmin):
    list_display = ('enterprise_name', 'yesterday_income', 'platform_income', 'settled_date')
    readonly_fields = ('appkey', 'secret')
    search_fields = ('enterprise_name',)

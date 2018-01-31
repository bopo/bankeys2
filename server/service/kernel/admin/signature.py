# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from service.signature.models import Signature


# @admin.register(Signature)
class SignatureAdmin(VersionAdmin):
    # 规则
    #  list_display = ('name','price')
    # list_editable = ('price',)
    pass

# admin.site.register(Certufucate, CertufucateAdmin)

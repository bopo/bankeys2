# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.usbkeys import Usb


class UsbAdmin(VersionAdmin):
    list_display = ('req_id', 'sin_data')


admin.site.register(Usb, UsbAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from service.kernel.models import Usb


class UsbSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(label=u'姓名')
    # idcard = serializers.CharField(label=u'身份证')

    class Meta:
        model = Usb
        fields = '__all__'

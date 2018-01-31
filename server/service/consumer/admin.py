# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from django.contrib.auth import get_user_model

from .models import Profile


# @admin.register(get_user_model())
# class ConsumerAdmin(admin.ModelAdmin):
#     list_display = ('username', 'date_joined', 'is_superuser', 'is_staff', 'is_active')
#     list_filter = ('is_superuser', 'is_staff', 'is_active')
#     search_fields = ('username', 'mobile')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'nick', 'gender', 'idcard', 'phone',)
    search_fields = ('name', 'nick', 'phone')
    list_filter = ('gender',)

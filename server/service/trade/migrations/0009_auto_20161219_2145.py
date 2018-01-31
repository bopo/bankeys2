# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0008_auto_20161219_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='transfer',
        ),
        migrations.AddField(
            model_name='transfer',
            name='payment',
            field=models.CharField(default='', max_length=100, verbose_name='\u652f\u4ed8\u8d26\u6237'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='receipt',
            field=models.CharField(default='', max_length=100, verbose_name='\u6536\u6b3e\u8d26\u6237'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='mobile',
            field=models.CharField(default='', max_length=100, verbose_name='\u5bf9\u65b9\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='receiver',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='summary',
            field=models.CharField(max_length=300, verbose_name='\u4ea4\u6613\u539f\u56e0'),
        ),
    ]

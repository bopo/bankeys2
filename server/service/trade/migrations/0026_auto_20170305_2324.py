# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-05 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0025_auto_20170305_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='account',
            field=models.CharField(default='', max_length=100, verbose_name='\u8f6c\u5165\u6237\u540d'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='bank_accountName',
            field=models.CharField(default=1, max_length=100, verbose_name='\u94f6\u884c\u5f00\u6237\u540d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='consumer',
            field=models.CharField(default='', max_length=100, verbose_name='\u6d88\u8d39\u5546\u5bb6'),
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
    ]
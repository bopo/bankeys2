# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0006_auto_20161124_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='consumption_type',
            field=models.CharField(choices=[(0, '\u626b\u7801\u652f\u4ed8'), (1, '\u7b2c\u4e09\u65b9\u652f\u4ed8')], default=0, max_length=100, verbose_name='\u6d88\u8d39\u7c7b\u578b'),
        ),
    ]
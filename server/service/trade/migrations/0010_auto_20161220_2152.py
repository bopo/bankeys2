# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0009_auto_20161219_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='type',
            field=models.CharField(choices=[('transfer', '\u8f6c\u8d26'), ('receiver', '\u6536\u6b3e'), ('thirty', '\u7b2c\u4e09\u65b9')], default=0, max_length=100, verbose_name='\u6d88\u8d39\u7c7b\u578b'),
        ),
    ]

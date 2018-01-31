# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0014_auto_20161130_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklist',
            name='black',
        ),
        migrations.RemoveField(
            model_name='blacklist',
            name='owner',
        ),
        migrations.AddField(
            model_name='contact',
            name='black',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u9ed1\u540d\u5355'),
        ),
        migrations.DeleteModel(
            name='Blacklist',
        ),
    ]
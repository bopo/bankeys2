# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-16 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0040_importexportitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImportExportItem',
            new_name='Video',
        ),
    ]

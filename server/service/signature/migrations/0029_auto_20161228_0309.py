# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0028_auto_20161227_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='backPhoto',
            field=models.ImageField(upload_to='identity', verbose_name='\u8bc1\u4ef6\u7167\u53cd\u9762'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='frontPhoto',
            field=models.ImageField(upload_to='identity', verbose_name='\u8bc1\u4ef6\u7167\u6b63\u9762'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-17 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0041_auto_20170416_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u5ba2\u670d',
                'verbose_name_plural': '\u5ba2\u670d',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '\u89c6\u9891', 'verbose_name_plural': '\u89c6\u9891'},
        ),
    ]
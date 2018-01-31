# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(verbose_name='\u7f16\u53f7')),
                ('transfer_type', models.CharField(choices=[(0, '\u6536\u6b3e'), (1, '\u8f6c\u8d26')], default=0, max_length=10, verbose_name='\u8f6c\u8d26\u7c7b\u578b')),
                ('transfer_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u8f6c\u8d26\u91d1\u989d')),
                ('receivables_bank', models.CharField(max_length=30, verbose_name='\u6536\u6b3e\u94f6\u884c')),
                ('receivables_lastNum', models.IntegerField(verbose_name='\u6536\u6b3e\u5c3e\u53f7')),
                ('drawee', models.CharField(max_length=100, verbose_name='\u4ed8\u6b3e\u4eba')),
                ('drawee_bank', models.CharField(max_length=30, verbose_name='\u4ed8\u6b3e\u94f6\u884c')),
                ('drawee_lastNum', models.IntegerField(verbose_name='\u4ed8\u6b3e\u5c3e\u53f7')),
                ('receivables_mark', models.TextField(null=True, verbose_name='\u8f6c\u8d26\u5907\u6ce8')),
                ('application_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('receipt_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7b7e\u6536\u65f6\u95f4')),
                ('confirm_transfer', models.BooleanField(default=False, verbose_name='\u786e\u8ba4\u8f6c\u8d26')),
                ('confirm_receipt', models.BooleanField(default=False, verbose_name='\u786e\u8ba4\u6536\u6b3e')),
            ],
            options={
                'verbose_name': '\u8f6c\u8d26\u8bb0\u5f55',
                'verbose_name_plural': '\u8f6c\u8d26\u8bb0\u5f55',
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0008_identity_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='originType',
            field=models.IntegerField(default='1', verbose_name='\u6e20\u9053\u7c7b\u578b '),
        ),
        migrations.AlterField(
            model_name='identity',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='backPhoto',
            field=models.ImageField(upload_to=b'', verbose_name='\u8bc1\u4ef6\u7167\u53cd\u9762'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='bankID',
            field=models.CharField(choices=[('542', '\u91cd\u5e86\u4e09\u5ce1\u94f6\u884c'), ('100', '\u90ae\u653f\u50a8\u84c4\u94f6\u884c'), ('102', '\u4e2d\u56fd\u5de5\u5546\u94f6\u884c'), ('103', '\u4e2d\u56fd\u519c\u4e1a\u94f6\u884c'), ('104', '\u4e2d\u56fd\u94f6\u884c'), ('105', '\u4e2d\u56fd\u5efa\u8bbe\u94f6\u884c'), ('301', '\u4ea4\u901a\u94f6\u884c'), ('302', '\u4e2d\u4fe1\u94f6\u884c'), ('303', '\u4e2d\u56fd\u5149\u5927\u94f6\u884c'), ('304', '\u534e\u590f\u94f6\u884c'), ('305', '\u4e2d\u56fd\u6c11\u751f\u94f6\u884c'), ('306', '\u5e7f\u4e1c\u53d1\u5c55\u94f6\u884c'), ('307', '\u5e73\u5b89\u94f6\u884c'), ('308', '\u62db\u5546\u94f6\u884c'), ('309', '\u5174\u4e1a\u94f6\u884c'), ('310', '\u4e0a\u6d77\u6d66\u4e1c\u53d1\u5c55\u94f6\u884c'), ('311', '\u6052\u4e30\u94f6\u884c'), ('316', '\u6d59\u5546\u94f6\u884c'), ('317', '\u6e24\u6d77\u94f6\u884c'), ('422', '\u6cb3\u5317\u94f6\u884c'), ('401', '\u4e0a\u6d77\u94f6\u884c'), ('403', '\u5317\u4eac\u94f6\u884c'), ('424', '\u5357\u4eac\u94f6\u884c'), ('423', '\u676d\u5dde\u94f6\u884c'), ('434', '\u5929\u6d25\u94f6\u884c'), ('408', '\u5b81\u6ce2\u94f6\u884c'), ('409', '\u9f50\u9c81\u94f6\u884c'), ('440', '\u5fbd\u5546\u94f6\u884c'), ('442', '\u54c8\u5c14\u6ee8\u94f6\u884c'), ('443', '\u8d35\u9633\u94f6\u884c'), ('447', '\u5170\u5dde\u94f6\u884c'), ('448', '\u5357\u660c\u94f6\u884c'), ('450', '\u9752\u5c9b\u94f6\u884c'), ('888', '\u4e2d\u91d1\u7f51\u94f6\u65e0\u5361'), ('889', '\u4e2d\u91d1\u7f51\u94f6'), ('891', '\u91d1\u79d1\u65e0\u5361'), ('892', '\u94f6\u8054\u4ee3\u6263'), ('900', '\u6536\u5355\u673a\u6784\uff08900\uff09'), ('700', 'CFCA\u6a21\u62df\u94f6\u884c'), ('1405', '\u5e7f\u4e1c\u519c\u5546\u884c'), ('1565', '\u9896\u6dee\u519c\u5546\u884c'), ('1513', '\u91cd\u5e86\u519c\u6751\u5546\u4e1a\u94f6\u884c')], default='542', max_length=100, verbose_name='\u94f6\u884cID'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='certId',
            field=models.CharField(default='', max_length=100, verbose_name='\u8bc1\u4ef6\u53f7'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='certType',
            field=models.IntegerField(default='1', verbose_name='\u8bc1\u4ef6\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='cvn2',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='\u4fe1\u7528\u5361\u80cc\u9762\u7684\u672b3\u4f4d\u6570\u5b57'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='expired',
            field=models.DateField(blank=True, null=True, verbose_name='\u6709\u6548\u671f'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='frontPhoto',
            field=models.ImageField(upload_to=b'', verbose_name='\u8bc1\u4ef6\u7167\u6b63\u9762'),
        ),
    ]

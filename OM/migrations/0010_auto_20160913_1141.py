# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM', '0009_auto_20160910_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servergroup',
            name='server_members',
            field=models.ManyToManyField(blank=True, null=True, to='OM.ServerList', verbose_name='\u4e0b\u5c5e\u670d\u52a1\u5668'),
        ),
    ]

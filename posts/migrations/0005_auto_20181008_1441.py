# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181008_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='author',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]

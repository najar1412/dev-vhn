# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashcore', '0004_auto_20160730_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='collect_asset',
            field=models.CharField(default='Not Set', max_length=100),
        ),
    ]

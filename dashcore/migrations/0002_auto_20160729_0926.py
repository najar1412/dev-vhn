# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 16:26
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='asset',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), null=True, size=None),
        ),
    ]
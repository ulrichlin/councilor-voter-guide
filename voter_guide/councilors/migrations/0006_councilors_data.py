# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 09:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('councilors', '0005_auto_20170322_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilors',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]

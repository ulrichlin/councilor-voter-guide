# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 06:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0011_add_candidate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='votes_detail',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]

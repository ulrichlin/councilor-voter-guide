# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0012_add_votes_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='occupy',
            field=models.NullBooleanField(db_index=True),
        ),
    ]

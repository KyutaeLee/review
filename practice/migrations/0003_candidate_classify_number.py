# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20180207_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='classify_number',
            field=models.IntegerField(default=0),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNAskApp', '0009_auto_20161118_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnprofile',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
    ]

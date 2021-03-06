# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNAskApp', '0007_cnquestion_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnanswer',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cnanswer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cnquestion',
            name='has_answers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cnquestion',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cnquestion',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cntag',
            name='questions',
            field=models.ManyToManyField(to='CNAskApp.CNQuestion'),
        ),
    ]

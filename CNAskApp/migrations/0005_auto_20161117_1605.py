# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 16:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('CNAskApp', '0004_auto_20161116_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnanswer',
            name='attachments',
            field=models.CharField(default='', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='cnanswer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNProfile'),
        ),
        migrations.AlterField(
            model_name='cnprofile',
            name='avatar',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cnprofile',
            name='info',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='cnprofile',
            name='status',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='cnquestion',
            name='attachments',
            field=models.CharField(default='', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='cnquestion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNProfile'),
        ),
        migrations.AlterField(
            model_name='cnquestion',
            name='full_text',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='cnquestion',
            name='short_text',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='cntag',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]

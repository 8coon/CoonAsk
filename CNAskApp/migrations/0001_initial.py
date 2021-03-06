# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 16:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CNAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_best', models.BooleanField(default=False)),
                ('full_text', models.TextField(max_length=10000)),
                ('images', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Прикреплённые изображения')),
            ],
        ),
        migrations.CreateModel(
            name='CNLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNAnswer')),
            ],
        ),
        migrations.CreateModel(
            name='CNProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_override', models.CharField(blank=True, max_length=100, verbose_name='Псевдоним')),
                ('avatar', models.BinaryField(max_length=4194304, null=True, verbose_name='Аватар')),
                ('status', models.TextField(max_length=255, verbose_name='Статус')),
                ('info', models.TextField(max_length=2000, verbose_name='Краткая информация')),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CNQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(max_length=10000, verbose_name='Полный текст')),
                ('short_text', models.TextField(max_length=300, verbose_name='Краткое описание')),
                ('images', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Прикреплённые изображения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNProfile', verbose_name='Профиль')),
            ],
        ),
        migrations.CreateModel(
            name='CNTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тег')),
            ],
        ),
        migrations.AddField(
            model_name='cnlike',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNProfile'),
        ),
        migrations.AddField(
            model_name='cnanswer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNProfile', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='cnanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CNAskApp.CNQuestion'),
        ),
        migrations.AddField(
            model_name='cnanswer',
            name='tags',
            field=models.ManyToManyField(to='CNAskApp.CNTag'),
        ),
    ]

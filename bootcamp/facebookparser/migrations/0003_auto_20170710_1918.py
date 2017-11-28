# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookparser', '0002_auto_20170709_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='group',
            name='cover',
            field=models.CharField(default='', max_length=150),
        ),
    ]
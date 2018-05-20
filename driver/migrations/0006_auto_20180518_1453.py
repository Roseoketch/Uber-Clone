# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='profilePic',
        ),
        migrations.AddField(
            model_name='driver',
            name='avatar',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
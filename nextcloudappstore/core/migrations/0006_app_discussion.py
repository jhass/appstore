# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160718_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='discussion',
            field=models.URLField(blank=True, max_length=256, verbose_name='Discussion'),
        ),
    ]

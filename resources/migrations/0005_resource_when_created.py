# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20170925_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='when_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='When created'),
            preserve_default=False,
        ),
    ]
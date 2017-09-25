# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20170925_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='categories',
            field=models.ManyToManyField(related_name='resources', to='resources.Resource', verbose_name='categories'),
        ),
        migrations.AddField(
            model_name='resource',
            name='main_image',
            field=models.ImageField(default='', upload_to='resources'),
            preserve_default=False,
        ),
    ]

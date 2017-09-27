# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_resource_when_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposeResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=100, verbose_name='Resource name')),
                ('resource_url', models.URLField(verbose_name='Resource URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveSmallIntegerField(default=0, help_text='Determines order of the resource. A product with a higher value will appear before one with a lower ranking.', verbose_name='Ranking')),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_recommendations', to='resources.Resource', verbose_name='Primary resource')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource', verbose_name='Recomend resource')),
            ],
            options={
                'verbose_name': 'Product related',
                'verbose_name_plural': 'Product related',
                'ordering': ['primary', '-ranking'],
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='related_items',
            field=models.ManyToManyField(blank=True, through='resources.RelatedResources', to='resources.Resource', verbose_name='Related resources'),
        ),
        migrations.AlterUniqueTogether(
            name='relatedresources',
            unique_together=set([('primary', 'recommendation')]),
        ),
    ]
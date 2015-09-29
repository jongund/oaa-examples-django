# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('category_num', models.IntegerField(unique=True)),
                ('category_id', models.CharField(max_length=64)),
                ('abbrev', models.CharField(max_length=2, default='x')),
                ('title', models.CharField(max_length=256)),
                ('title_plural', models.CharField(max_length=256, verbose_name='Title Plural')),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField()),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order', 'title'],
                'verbose_name': 'Rule Category',
                'verbose_name_plural': 'Rule Categories',
            },
        ),
    ]

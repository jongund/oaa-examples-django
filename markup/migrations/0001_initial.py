# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElementDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('element', models.CharField(max_length=30, blank=True, null=True)),
                ('attribute', models.CharField(max_length=30, blank=True, null=True)),
                ('value', models.CharField(max_length=60, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(default='N', max_length=1, choices=[('N', 'not any special type'), ('R', 'ARIA Role'), ('P', 'ARIA Property'), ('S', 'ARIA State'), ('E', 'Event'), ('F', 'Font'), ('C', 'Color'), ('O', 'Position'), ('H', 'Highlight')])),
            ],
            options={
                'verbose_name': 'Element Definition',
                'verbose_name_plural': 'Element Definitions',
                'ordering': ['element', 'attribute', 'value'],
            },
        ),
        migrations.CreateModel(
            name='LanguageSpec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('abbr', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('element_based', models.BooleanField(default=True, verbose_name='Element based markup (otherwise property based, i.e. CSS)')),
                ('url', models.URLField()),
                ('url_slug', models.SlugField(max_length=32)),
                ('link_text', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Language Specification',
                'verbose_name_plural': 'Language Specifications',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='elementdefinition',
            name='spec',
            field=models.ForeignKey(related_name='element_definitions', to='markup.LanguageSpec'),
        ),
    ]

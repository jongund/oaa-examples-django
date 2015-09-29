# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('updated_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='abouts.Updated')),
                ('about_id', models.AutoField(primary_key=True, serialize=False)),
                ('about_slug', models.SlugField(null=True, blank=True)),
                ('title', models.CharField(max_length=512, verbose_name='About Title')),
                ('title_html', models.CharField(max_length=1024, default='')),
                ('title_text', models.CharField(max_length=512, default='')),
                ('content', models.TextField(null=True, verbose_name='Content (textile markup)', blank=True)),
                ('content_html', models.TextField(null=True, blank=True, default='')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Abouts',
                'verbose_name': 'About',
                'ordering': ['order'],
            },
            bases=('abouts.updated',),
        ),
    ]

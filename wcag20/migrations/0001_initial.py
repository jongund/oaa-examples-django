# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WCAG20_Guideline',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'WCAG 2.0 Guidelines',
                'verbose_name': 'WCAG 2.0 Guideline',
                'ordering': ['principle__num', 'num'],
            },
        ),
        migrations.CreateModel(
            name='WCAG20_Principle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'WCAG 2.0 Principles',
                'verbose_name': 'WCAG 2.0 Principle',
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='WCAG20_SuccessCriterion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.TextField()),
                ('level', models.CharField(choices=[('1', 'Level A'), ('2', 'Level AA'), ('3', 'Level AAA')], max_length=2)),
                ('num', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
                ('url_meet', models.URLField(blank=True, null=True)),
                ('url_understand', models.URLField(blank=True, null=True)),
                ('guideline', models.ForeignKey(related_name='success_criteria', to='wcag20.WCAG20_Guideline')),
            ],
            options={
                'verbose_name_plural': 'WCAG 2.0 Success Criteria',
                'verbose_name': 'WCAG 2.0 Success Criterion',
                'ordering': ['guideline__principle__num', 'guideline__num', 'num'],
            },
        ),
        migrations.AddField(
            model_name='wcag20_guideline',
            name='principle',
            field=models.ForeignKey(related_name='guidelines', to='wcag20.WCAG20_Principle'),
        ),
    ]

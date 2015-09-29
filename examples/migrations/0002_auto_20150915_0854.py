# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualcheck',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='manualcheck',
            name='updated_ptr',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='rule_category',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='target_resources',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='updated_ptr',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='wcag_primary',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='wcag_related',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='updated_ptr',
        ),
        migrations.RemoveField(
            model_name='example',
            name='onload',
        ),
        migrations.RemoveField(
            model_name='example',
            name='title_override',
        ),
        migrations.RemoveField(
            model_name='updated',
            name='updated_editor',
        ),
        migrations.DeleteModel(
            name='ManualCheck',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.DeleteModel(
            name='Technique',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-15 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_plan_junit_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='sfdx_config',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0005_auto_20161213_1938'),
        ('testresults', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testexecution',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='testexecution',
            name='build',
        ),
        migrations.RemoveField(
            model_name='testexecution',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='testexecution',
            name='repository',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='execution',
        ),
        migrations.AddField(
            model_name='testresult',
            name='build',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='build.Build'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='testresults.TestMethod'),
        ),
        migrations.DeleteModel(
            name='TestEnvironment',
        ),
        migrations.DeleteModel(
            name='TestExecution',
        ),
    ]
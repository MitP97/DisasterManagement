# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-16 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180316_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemusers',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
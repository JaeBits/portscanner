# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-11 22:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='active',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='scan',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 11, 22, 2, 9, 561154)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='last_run',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 11, 22, 2, 9, 561154)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ip', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
                ('ip', models.ForeignKey(null=True, to='scanner.Ip', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 3, 11, 13, 2, 18, 536148))),
                ('last_run', models.DateTimeField(default=datetime.datetime(2017, 3, 11, 13, 2, 18, 536148))),
            ],
        ),
        migrations.AddField(
            model_name='ip',
            name='scan',
            field=models.ForeignKey(to='scanner.Scan'),
        ),
    ]

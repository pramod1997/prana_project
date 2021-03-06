# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prana_forecast', '0002_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_param1', models.FloatField(default=0.0)),
                ('hw_param2', models.FloatField(default=0.0)),
                ('hw_param3', models.FloatField(default=0.0)),
                ('c_param1', models.FloatField(default=0.0)),
                ('c_param2', models.FloatField(default=0.0)),
                ('fb_prophet_param1', models.FloatField(default=0.0)),
                ('arima_param1', models.FloatField(default=0.0)),
            ],
        ),
    ]

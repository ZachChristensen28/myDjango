# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 05:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180104_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 5, 25, 8, 16050, tzinfo=utc)),
        ),
    ]
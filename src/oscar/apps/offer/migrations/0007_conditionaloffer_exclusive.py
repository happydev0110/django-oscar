# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-04 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_auto_20170504_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditionaloffer',
            name='exclusive',
            field=models.BooleanField(default=True, help_text='Exclusive offers cannot be combined on the same items', verbose_name='Exclusive offer'),
        ),
    ]

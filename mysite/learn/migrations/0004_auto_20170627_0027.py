# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Data',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Sensor',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Sensor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0010_auto_20171114_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]

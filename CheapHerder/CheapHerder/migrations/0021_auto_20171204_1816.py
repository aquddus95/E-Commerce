# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0020_auto_20171204_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='product_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Product_Price'),
        ),
    ]
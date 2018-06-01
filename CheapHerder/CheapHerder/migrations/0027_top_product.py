# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0026_create_custom_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='top_product',
            fields=[
                ('item_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'top_prod',
                'managed': False,
            },
        ),
    ]

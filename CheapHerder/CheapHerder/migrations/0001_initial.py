# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('upc', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('p_type', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('colors', models.CharField(max_length=255)),
                ('materials', models.CharField(max_length=255)),
                ('attributes', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('category_id', models.IntegerField()),
                ('unit_weight', models.DecimalField(decimal_places=10, max_digits=10)),
                ('category', models.CharField(max_length=200)),
                ('subcategory_id', models.IntegerField()),
                ('subcategory', models.CharField(max_length=200)),
                ('inventory', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('image_url', models.CharField(max_length=200)),
                ('supplier_id', models.CharField(max_length=200)),
            ],
        ),
    ]

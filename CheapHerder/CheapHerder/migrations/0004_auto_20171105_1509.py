# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0003_auto_20171028_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('shipping_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('cc_expiry', models.CharField(max_length=100)),
                ('cc_number', models.CharField(max_length=200)),
                ('cc_ccv', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pledges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Group')),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Organization')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Search_Item',
            fields=[
                ('search_id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.TextField()),
                ('created', models.DateTimeField()),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=5, max_digits=10)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Supplier'),
        ),
        migrations.AddField(
            model_name='group',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Product'),
        ),
        migrations.AddField(
            model_name='group',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Transaction'),
        ),
    ]

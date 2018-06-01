# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0029_create_custom_sp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1024)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheapHerder.Group')),
            ],
        ),
        migrations.AddField(
            model_name='pledge',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]

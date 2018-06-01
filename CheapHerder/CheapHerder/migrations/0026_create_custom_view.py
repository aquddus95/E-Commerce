# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0025_create_custom_view'),
    ]

    operations = [
	migrations.RunSQL("""CREATE VIEW top_prod AS select count("CheapHerder_group".group_id) as groupcount,"CheapHerder_product".item_code,"CheapHerder_product".product_name,"CheapHerder_product".description,"CheapHerder_product".image_url  from "CheapHerder_product" left outer join "CheapHerder_group" on "CheapHerder_product".item_code= "CheapHerder_group".product_id_id Group BY "CheapHerder_product".item_code,"CheapHerder_product".product_name,"CheapHerder_product".description,"CheapHerder_product".image_url ORDER BY groupcount DESC limit 4;""")
    ]

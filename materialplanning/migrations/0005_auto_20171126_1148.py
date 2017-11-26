# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materialplanning', '0004_auto_20171124_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier_email',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier_Contact_Person'),
        ),
        migrations.AlterField(
            model_name='supplier_landline_number',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier_Contact_Person'),
        ),
        migrations.AlterField(
            model_name='supplier_mobile_number',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier_Contact_Person'),
        ),
    ]

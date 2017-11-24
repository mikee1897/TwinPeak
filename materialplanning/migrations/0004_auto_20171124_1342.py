# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productdevelopment', '0002_auto_20171124_1342'),
        ('materialplanning', '0003_auto_20171124_1342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.DeleteModel(
            name='Part_In',
        ),
        migrations.DeleteModel(
            name='Part_Out',
        ),
        migrations.DeleteModel(
            name='Purchase_Order',
        ),
        migrations.DeleteModel(
            name='Purchase_Order_Item',
        ),
        migrations.AddField(
            model_name='supplier_mobile_number',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier'),
        ),
        migrations.AddField(
            model_name='supplier_landline_number',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier'),
        ),
        migrations.AddField(
            model_name='supplier_email',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier'),
        ),
        migrations.AddField(
            model_name='supplier_contact_person',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier'),
        ),
        migrations.AddField(
            model_name='raw_material_exit',
            name='raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Raw_Material'),
        ),
        migrations.AddField(
            model_name='raw_material_entry',
            name='raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Raw_Material'),
        ),
        migrations.AddField(
            model_name='raw_material',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Supplier'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productdevelopment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Contact_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Landline_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landline_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Mobile_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Labor_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutting_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('sewing_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('washing_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('finishing_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('examining_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('pressing_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('packaging_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('final_inspection_cost', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Overhead_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('utility_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('paper_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('machine_maintenance_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('transportation_gas_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('transportation_maintenance_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('communication_cost', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Size_Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=500)),
                ('style_id', models.CharField(max_length=500)),
                ('collection_name', models.CharField(max_length=500)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Style_Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='deliverable',
        ),
        migrations.RemoveField(
            model_name='costing',
            name='order',
        ),
        migrations.RemoveField(
            model_name='costing_parts',
            name='costing',
        ),
        migrations.RemoveField(
            model_name='costing_parts',
            name='part',
        ),
        migrations.RenameField(
            model_name='deliverable',
            old_name='end_date',
            new_name='end_delivery_date',
        ),
        migrations.RenameField(
            model_name='deliverable',
            old_name='start_date',
            new_name='start_delivery_date',
        ),
        migrations.RenameField(
            model_name='operations',
            old_name='operation',
            new_name='operation_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='order',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='program_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='style_number',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='purchase_order_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='size',
            field=models.CharField(choices=[('32A', '32A'), ('32B', '32B'), ('34A', '34A'), ('34B', '34B'), ('36A', '36A'), ('36B', '36B')], max_length=5),
        ),
        migrations.AlterField(
            model_name='operations',
            name='minutes',
            field=models.IntegerField(),
        ),
    ]

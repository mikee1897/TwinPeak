# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materialplanning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=10, max_digits=19)),
                ('finished', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Costing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labor_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('overhead_cost', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Costing_Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.CharField(max_length=500)),
                ('costing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Costing')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialplanning.Part')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('contact_number', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('size', models.CharField(choices=[('32A,', '32A,'), ('32B', '32B'), ('34A', '34A'), ('34B', '34B'), ('36A', '36A'), ('36B', '36B')], max_length=5)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('operation', models.CharField(max_length=500)),
                ('material', models.CharField(max_length=500)),
                ('stitch', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('minutes', models.CharField(max_length=500)),
                ('machine', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=100)),
                ('collection', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('style_number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='operations',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Order'),
        ),
        migrations.AddField(
            model_name='deliverable',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Order'),
        ),
        migrations.AddField(
            model_name='costing',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Order'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='deliverable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdevelopment.Deliverable'),
        ),
    ]

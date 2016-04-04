# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribtions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('Appartment', 'Appartment'), ('Building', 'Building'), ('Land', 'Land'), ('Villa', 'Villa'), ('Store', 'Store'), ('Office', 'Office')], max_length=50)),
                ('property_categories', models.CharField(choices=[('s', 'For Sale'), ('r', 'For Rent')], max_length=1)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

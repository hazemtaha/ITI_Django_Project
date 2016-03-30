# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.4 on 2016-03-28 20:08
=======
# Generated by Django 1.9.4 on 2016-03-30 08:02
>>>>>>> 6861b14749aa793cea12a53c76b2a876339ad2c2
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('a', 'Appartment'), ('b', 'Building'), ('l', 'Land'), ('v', 'Villa'), ('s', 'Store'), ('o', 'Office')], max_length=1)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('min_size', models.FloatField()),
                ('max_size', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('location_desc', models.TextField()),
                ('services', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
            ],
        ),
        migrations.AddField(
            model_name='projectproperties',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects'),
        ),
        migrations.AddField(
            model_name='projectphotos',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects'),
        ),
    ]

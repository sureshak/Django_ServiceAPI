# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angular2_backEnd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20, unique=True)),
                ('Mobile', models.CharField(max_length=20, unique=True)),
                ('Password', models.CharField(max_length=20)),
                ('Pincode', models.CharField(max_length=20)),
            ],
        ),
    ]

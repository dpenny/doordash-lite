# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddl', '0002_auto_20170503_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='cover',
            field=models.ImageField(default='static/stores/3.jpg', upload_to='static/stores', verbose_name='店铺封面'),
        ),
    ]

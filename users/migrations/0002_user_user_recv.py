# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_recv',
            field=models.CharField(default='', max_length=20),
        ),
    ]
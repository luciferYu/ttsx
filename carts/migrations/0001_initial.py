# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_userbrowsehistory'),
        ('goods', '0003_goodsinfo_goods_invetory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_delete', models.BooleanField(default=False)),
                ('cart_amount', models.IntegerField()),
                ('cart_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

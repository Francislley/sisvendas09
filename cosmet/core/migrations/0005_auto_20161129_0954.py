# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161121_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque_entrada',
            field=models.IntegerField(verbose_name='Estoque de entrada'),
        ),
    ]

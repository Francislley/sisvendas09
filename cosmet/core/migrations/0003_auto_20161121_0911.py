# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_produto_qtd_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estoque_atual', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='qtd_estoque',
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_entrada',
            field=models.IntegerField(default=0, verbose_name='Estoque de entrada'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribbonwish', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]

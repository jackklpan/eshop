# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20161129_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(blank=True, to='books.Tag', verbose_name='標籤'),
        ),
    ]
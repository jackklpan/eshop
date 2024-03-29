# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('original_price', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '未上架'), (1, '上架中'), (2, '已下架')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True)),
                ('author', models.CharField(max_length=100)),
                ('translator', models.CharField(blank=True, default='', max_length=100)),
                ('publisher', models.CharField(blank=True, default='', max_length=100)),
                ('isbn', models.CharField(blank=True, default='', max_length=13)),
                ('language', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(null=True, to='books.Tag'),
        ),
    ]

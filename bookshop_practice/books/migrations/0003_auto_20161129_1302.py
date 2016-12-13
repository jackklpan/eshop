# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20161129_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '書籍', 'verbose_name_plural': '書籍'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分類', 'verbose_name_plural': '分類'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '標籤', 'verbose_name_plural': '標籤'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Category', verbose_name='分類'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='新增時間'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='內容簡介'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, default='', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='語言'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名稱'),
        ),
        migrations.AlterField(
            model_name='book',
            name='original_price',
            field=models.PositiveIntegerField(default=0, verbose_name='原價'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='售價'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(null=True, verbose_name='上架時間'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '未上架'), (1, '上架中'), (2, '已下架')], default=0, verbose_name='狀態'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(to='books.Tag', verbose_name='標籤'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='譯者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新時間'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='分類名稱'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='標籤名稱'),
        ),
    ]

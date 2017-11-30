# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=50, db_index=True)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, help_text='根据name生成的，用于生成页面URL，必须唯一')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=255, unique=True, db_index=True)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=255, unique=True, help_text='根据name生成的，用于生成页面URL，必须唯一')),
                ('price', models.DecimalField(verbose_name='价格', max_digits=9, decimal_places=2)),
                ('image', models.ImageField(verbose_name='图片', max_length=50, blank=True, upload_to='products/%Y/%m/%d')),
                ('is_available', models.BooleanField(verbose_name='是否有', default=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('categories', models.ManyToManyField(related_name='products', to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ('name',),
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='df_goods')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit', models.CharField(max_length=20)),
                ('repertroy', models.IntegerField()),
                ('click', models.IntegerField()),
                ('intro', models.CharField(max_length=200)),
                ('context', tinymce.models.HTMLField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='typeInfo',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]

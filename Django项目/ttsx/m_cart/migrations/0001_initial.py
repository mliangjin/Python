# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_goods', '0001_initial'),
        ('m_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('goods', models.ForeignKey(to='m_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='m_user.UserInfo')),
            ],
        ),
    ]

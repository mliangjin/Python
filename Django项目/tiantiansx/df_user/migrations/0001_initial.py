# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=20)),
                ('shou', models.CharField(max_length=20, null=True)),
                ('detaddr', models.CharField(max_length=100, null=True)),
                ('youbian', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]

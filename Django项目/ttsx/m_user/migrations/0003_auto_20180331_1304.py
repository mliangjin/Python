# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_user', '0002_auto_20180331_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='youbian',
            field=models.CharField(max_length=6, null=True),
        ),
    ]

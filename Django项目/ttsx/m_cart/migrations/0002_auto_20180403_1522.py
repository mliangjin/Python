# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]

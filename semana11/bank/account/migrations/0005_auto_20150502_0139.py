# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_account_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='account',
            name='value',
        ),
        migrations.AlterField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]

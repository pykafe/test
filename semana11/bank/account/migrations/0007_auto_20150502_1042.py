# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20150502_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='period',
        ),
        migrations.RemoveField(
            model_name='account',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='account',
            name='value',
        ),
    ]

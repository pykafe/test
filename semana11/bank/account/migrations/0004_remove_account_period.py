# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150428_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='period',
        ),
    ]

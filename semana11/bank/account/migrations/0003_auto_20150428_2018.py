# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150425_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='period',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='rate',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='value',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]

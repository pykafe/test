# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150502_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='period',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='rate',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='value',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]

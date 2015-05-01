# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0002_auto_20150501_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='dodgeAC',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='naturalAC',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

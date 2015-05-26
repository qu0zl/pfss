# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0031_auto_20150520_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='bonusToDmg',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

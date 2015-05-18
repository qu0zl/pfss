# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0026_creaturegroup_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialability',
            name='dynamicShortText',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

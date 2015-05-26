# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0035_creatureattack_extraattackatfullbab'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureattack',
            name='noIterative',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

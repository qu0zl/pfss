# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0043_creature_supportedextratype'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureattack',
            name='makePrimary',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

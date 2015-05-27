# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0038_creature_deflectac'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureattack',
            name='touchAttack',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

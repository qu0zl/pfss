# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0017_attack_crit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creatureattack',
            options={'ordering': ['creature', 'exclusive']},
        ),
        migrations.AddField(
            model_name='creatureattack',
            name='exclusive',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

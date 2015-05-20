# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0030_creatureattack_makesecondary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creatureattack',
            options={'ordering': ['creature', 'exclusive', 'attack__attackClass']},
        ),
        migrations.AddField(
            model_name='creature',
            name='Space',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]

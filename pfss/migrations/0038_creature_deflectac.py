# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0037_creatureattack_wield2handed'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='deflectAC',
            field=models.IntegerField(default=0, verbose_name=b'Deflection AC Bonus'),
            preserve_default=True,
        ),
    ]

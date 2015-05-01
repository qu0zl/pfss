# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0006_auto_20150501_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='attackClass',
            field=models.IntegerField(default=0, choices=[(0, b'Primary'), (1, b'Secondary'), (2, b'Manufactured')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attack',
            name='attackType',
            field=models.IntegerField(default=0, choices=[(0, b'Melee'), (1, b'Ranged')]),
            preserve_default=True,
        ),
    ]

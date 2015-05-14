# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0015_creatureextratype_senses'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='rangedStrOption',
            field=models.IntegerField(default=2, choices=[(1, b"Don't add Str"), (2, b'Add Str'), (3, b'Add Str if negative')]),
            preserve_default=True,
        ),
    ]

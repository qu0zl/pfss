# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0002_auto_20150507_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='creaturetype',
            name='BAB_Progression',
            field=models.IntegerField(default=2, choices=[(1, b'Slow'), (2, b'Medium'), (3, b'Fast')]),
            preserve_default=True,
        ),
    ]

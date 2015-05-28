# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0039_creatureattack_touchattack'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='baseName',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
    ]

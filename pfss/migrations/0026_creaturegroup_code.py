# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0025_specialability_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='creaturegroup',
            name='code',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
    ]

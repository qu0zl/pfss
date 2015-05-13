# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0014_creaturegroup_defaultextratype'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureextratype',
            name='Senses',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]

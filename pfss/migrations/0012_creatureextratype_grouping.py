# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0011_creaturegroup_allowedextratype'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureextratype',
            name='Grouping',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]

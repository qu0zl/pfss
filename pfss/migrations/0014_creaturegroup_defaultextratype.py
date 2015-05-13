# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0013_auto_20150513_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='creaturegroup',
            name='DefaultExtraType',
            field=models.ManyToManyField(related_name='DefaultCreatureExtraType_set', null=True, to='pfss.CreatureExtraType', blank=True),
            preserve_default=True,
        ),
    ]

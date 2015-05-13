# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0010_auto_20150512_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='creaturegroup',
            name='AllowedExtraType',
            field=models.ManyToManyField(to='pfss.CreatureExtraType', null=True, blank=True),
            preserve_default=True,
        ),
    ]

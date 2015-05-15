# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0022_creature_nosummontemplates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attack',
            options={'ordering': ['attackType', 'attackClass', 'name']},
        ),
        migrations.AlterModelOptions(
            name='creaturegroup',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='creature',
            name='extraACText',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='extraWillText',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

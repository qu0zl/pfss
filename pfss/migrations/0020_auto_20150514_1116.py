# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0019_specialability_isattack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creatureskill',
            options={'ordering': ['creature', 'skill']},
        ),
        migrations.AddField(
            model_name='creaturetype',
            name='Immune',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialability',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

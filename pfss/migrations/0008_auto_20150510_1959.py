# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0007_creature_cmbtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='DefenseText',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='OffenseText',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0023_auto_20150515_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialability',
            name='isDefense',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialability',
            name='isGeneral',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

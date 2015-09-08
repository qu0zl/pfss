# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0042_auto_20150602_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='SupportedExtraType',
            field=models.ManyToManyField(default=None, related_name='SupportedExtraType_set', null=True, to='pfss.CreatureExtraType', blank=True),
            preserve_default=True,
        ),
    ]

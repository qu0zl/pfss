# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0032_attack_bonustodmg'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='extraHPText',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

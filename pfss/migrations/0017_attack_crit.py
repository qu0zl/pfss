# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0016_attack_rangedstroption'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='crit',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
    ]

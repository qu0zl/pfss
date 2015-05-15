# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0024_auto_20150515_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialability',
            name='short',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

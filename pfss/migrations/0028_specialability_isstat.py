# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0027_specialability_dynamicshorttext'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialability',
            name='isStat',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

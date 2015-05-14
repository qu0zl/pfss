# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0018_auto_20150514_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialability',
            name='isAttack',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

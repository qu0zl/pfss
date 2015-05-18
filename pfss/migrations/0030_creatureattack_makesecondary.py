# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0029_auto_20150518_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatureattack',
            name='makeSecondary',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

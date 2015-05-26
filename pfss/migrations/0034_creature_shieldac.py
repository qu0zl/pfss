# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0033_creature_extrahptext'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='shieldAC',
            field=models.IntegerField(default=0, verbose_name=b'Shield AC Bonus'),
            preserve_default=True,
        ),
    ]

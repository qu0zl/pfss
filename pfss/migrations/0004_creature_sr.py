# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0003_creaturetype_bab_progression'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='SR',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

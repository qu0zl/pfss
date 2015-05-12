# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0009_auto_20150510_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='CRdenom',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='CRnum',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]

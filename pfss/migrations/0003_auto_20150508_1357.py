# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0002_auto_20150508_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupentry',
            name='Augmented',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='groupentry',
            name='text',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

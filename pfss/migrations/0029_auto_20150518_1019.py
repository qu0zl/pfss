# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0028_specialability_isstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='bonusToHit',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attack',
            name='attackClass',
            field=models.IntegerField(default=0, choices=[(0, b'Primary'), (1, b'Secondary'), (2, b'Light'), (3, b'One Handed'), (4, b'Two Handed')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0020_auto_20150514_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feat',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='creature',
            name='dodgeAC',
        ),
        migrations.AddField(
            model_name='creaturetype',
            name='Weaknesses',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

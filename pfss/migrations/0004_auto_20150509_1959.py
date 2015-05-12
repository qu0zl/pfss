# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0003_auto_20150508_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creature',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='creatureattack',
            options={'ordering': ['creature']},
        ),
        migrations.AlterModelOptions(
            name='creatureskill',
            options={'ordering': ['creature']},
        ),
        migrations.AlterModelOptions(
            name='creaturetype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='creature',
            name='CMDText',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

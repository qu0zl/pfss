# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0012_creatureextratype_grouping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creatureextratype',
            options={'ordering': ['Grouping', 'name']},
        ),
        migrations.RemoveField(
            model_name='groupentry',
            name='Augmented',
        ),
        migrations.AddField(
            model_name='creaturegroup',
            name='Augmented',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creatureextratype',
            name='Grouping',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]

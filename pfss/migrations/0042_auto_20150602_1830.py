# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0041_auto_20150602_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creaturegroup',
            options={'ordering': ['Grouping', 'name']},
        ),
        migrations.AlterField(
            model_name='creaturegroup',
            name='Grouping',
            field=models.ForeignKey(default=3, to='pfss.Grouping'),
            preserve_default=False,
        ),
    ]

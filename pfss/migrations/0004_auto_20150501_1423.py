# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0003_auto_20150501_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='armourAC',
            field=models.IntegerField(default=0, verbose_name=b'Armour Bonus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='HD',
            field=models.IntegerField(verbose_name=b'Hit-Dice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='dodgeAC',
            field=models.IntegerField(default=0, verbose_name=b'Dodge AC Bonus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='naturalAC',
            field=models.IntegerField(default=0, verbose_name=b'Natural AC Bonus'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0005_auto_20150509_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='HDtype',
        ),
        migrations.AddField(
            model_name='creaturetype',
            name='HDtype',
            field=models.ForeignKey(default=None, blank=True, to='pfss.Die', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creatureextratype',
            name='Defense',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creatureextratype',
            name='Offense',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]

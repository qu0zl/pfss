# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='BAB',
        ),
        migrations.AlterField(
            model_name='creature',
            name='Attacks',
            field=models.ManyToManyField(to='pfss.Attack', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='HD',
            field=models.IntegerField(null=True, verbose_name=b'Hit-Dice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='Special',
            field=models.ManyToManyField(default=None, to='pfss.SpecialAbility', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creaturetype',
            name='GoodSave1',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creaturetype',
            name='GoodSave2',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creaturetype',
            name='GoodSave3',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')]),
            preserve_default=True,
        ),
    ]

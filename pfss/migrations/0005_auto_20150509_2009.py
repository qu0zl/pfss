# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0004_auto_20150509_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatureExtraType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('Defense', models.CharField(max_length=256)),
                ('Offense', models.CharField(max_length=256)),
                ('Special', models.ManyToManyField(to='pfss.SpecialAbility', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creature',
            name='ExtraType',
            field=models.ManyToManyField(default=None, to='pfss.CreatureExtraType', null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatureGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=128)),
                ('Group', models.ForeignKey(to='pfss.CreatureGroup')),
                ('creature', models.ForeignKey(to='pfss.Creature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creature',
            name='Groups',
            field=models.ManyToManyField(to='pfss.CreatureGroup', null=True, through='pfss.GroupEntry', blank=True),
            preserve_default=True,
        ),
    ]

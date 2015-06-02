# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0040_attack_basename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('priority', models.IntegerField(default=0, null=True, blank=True)),
            ],
            options={
                'ordering': ['priority', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='specialability',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='creaturegroup',
            name='Grouping',
            field=models.ForeignKey(default=None, to='pfss.Grouping', null=True),
            preserve_default=True,
        ),
    ]

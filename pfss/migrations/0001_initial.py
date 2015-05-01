# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('Str', models.IntegerField()),
                ('Dex', models.IntegerField()),
                ('Con', models.IntegerField()),
                ('Int', models.IntegerField()),
                ('Wis', models.IntegerField()),
                ('Cha', models.IntegerField()),
                ('BAB', models.IntegerField()),
                ('HD', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Die',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creature',
            name='HDtype',
            field=models.ForeignKey(default=None, to='pfss.Die'),
            preserve_default=True,
        ),
    ]

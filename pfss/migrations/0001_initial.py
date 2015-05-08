# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('dCount', models.IntegerField(default=1)),
                ('attackType', models.IntegerField(default=0, choices=[(0, b'Melee'), (1, b'Ranged'), (2, b'SPECIAL')])),
                ('attackClass', models.IntegerField(default=0, choices=[(0, b'Primary'), (1, b'Secondary'), (2, b'Light'), (3, b'One Handed'), (b'TWO_HANDED', b'Two Handed')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
                ('SR', models.IntegerField(default=0)),
                ('Speed', models.CharField(max_length=256, blank=True)),
                ('HD', models.IntegerField(null=True, verbose_name=b'Hit-Dice')),
                ('armourAC', models.IntegerField(default=0, verbose_name=b'Armour Bonus')),
                ('naturalAC', models.IntegerField(default=0, verbose_name=b'Natural AC Bonus')),
                ('dodgeAC', models.IntegerField(default=0, verbose_name=b'Dodge AC Bonus')),
                ('Senses', models.CharField(max_length=256, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatureAttack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extraText', models.TextField(null=True, blank=True)),
                ('count', models.IntegerField(default=1)),
                ('attack', models.ForeignKey(to='pfss.Attack')),
                ('creature', models.ForeignKey(to='pfss.Creature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatureSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extraText', models.TextField(null=True, blank=True)),
                ('extraModifier', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('creature', models.ForeignKey(to='pfss.Creature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatureType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('BAB_Progression', models.IntegerField(default=2, choices=[(1, b'Slow'), (2, b'Medium'), (3, b'Fast')])),
                ('GoodSave1', models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')])),
                ('GoodSave2', models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')])),
                ('GoodSave3', models.IntegerField(default=None, null=True, blank=True, choices=[(None, b'None'), (1, b'Fortitude'), (2, b'Reflex'), (3, b'Will')])),
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
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('ACbonus', models.IntegerField()),
                ('reach', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('stat', models.IntegerField(choices=[(1, b'Strength'), (2, b'Dexterity'), (3, b'Constitution'), (4, b'Intelligence'), (5, b'Wisdom'), (6, b'Charisma')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialAbility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('dynamicText', models.BooleanField(default=False)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creatureskill',
            name='skill',
            field=models.ForeignKey(to='pfss.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Attacks',
            field=models.ManyToManyField(to='pfss.Attack', null=True, through='pfss.CreatureAttack', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Feats',
            field=models.ManyToManyField(to='pfss.Feat', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='HDtype',
            field=models.ForeignKey(default=None, to='pfss.Die'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Languages',
            field=models.ManyToManyField(to='pfss.Language', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Size',
            field=models.ForeignKey(default=None, to='pfss.Size'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Skills',
            field=models.ManyToManyField(default=None, to='pfss.Skill', through='pfss.CreatureSkill', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Special',
            field=models.ManyToManyField(default=None, to='pfss.SpecialAbility', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creature',
            name='Type',
            field=models.ForeignKey(default=None, to='pfss.CreatureType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attack',
            name='dType',
            field=models.ForeignKey(default=None, to='pfss.Die'),
            preserve_default=True,
        ),
    ]

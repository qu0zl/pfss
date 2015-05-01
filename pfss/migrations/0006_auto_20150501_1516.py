# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0005_creature_speed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('dCount', models.IntegerField(default=1)),
                ('attackType', models.IntegerField(default=0, choices=[(0, b'Primary'), (1, b'Secondary'), (2, b'Manufactured')])),
                ('dType', models.ForeignKey(default=None, to='pfss.Die')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creature',
            name='Attacks',
            field=models.ManyToManyField(to='pfss.Attack'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creature',
            name='Speed',
            field=models.IntegerField(default=30, choices=[(5, b'5'), (10, b'10'), (15, b'15'), (20, b'20'), (25, b'25'), (30, b'30'), (35, b'35'), (40, b'40'), (45, b'45'), (50, b'50'), (55, b'55'), (60, b'60'), (65, b'65'), (70, b'70'), (75, b'75'), (80, b'80'), (85, b'85'), (90, b'90'), (95, b'95'), (100, b'100'), (105, b'105'), (110, b'110'), (115, b'115'), (120, b'120'), (125, b'125'), (130, b'130'), (135, b'135'), (140, b'140'), (145, b'145'), (150, b'150'), (155, b'155'), (160, b'160'), (165, b'165'), (170, b'170'), (175, b'175'), (180, b'180'), (185, b'185'), (190, b'190'), (195, b'195'), (200, b'200'), (205, b'205'), (210, b'210'), (215, b'215'), (220, b'220'), (225, b'225'), (230, b'230'), (235, b'235'), (240, b'240'), (245, b'245'), (250, b'250'), (255, b'255'), (260, b'260'), (265, b'265'), (270, b'270'), (275, b'275'), (280, b'280'), (285, b'285'), (290, b'290'), (295, b'295')]),
            preserve_default=True,
        ),
    ]

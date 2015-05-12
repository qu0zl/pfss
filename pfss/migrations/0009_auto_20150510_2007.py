# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0008_auto_20150510_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('short', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='creature',
            name='Alignment',
            field=models.ForeignKey(default=None, to='pfss.Alignment', null=True),
            preserve_default=True,
        ),
    ]

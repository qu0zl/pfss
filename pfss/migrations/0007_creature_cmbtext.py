# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0006_auto_20150509_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='CMBText',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]

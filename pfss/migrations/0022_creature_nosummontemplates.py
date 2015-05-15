# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfss', '0021_auto_20150514_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='NoSummonTemplates',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150322_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='color',
            field=models.TextField(default='FFFFFF'),
            preserve_default=False,
        ),
    ]

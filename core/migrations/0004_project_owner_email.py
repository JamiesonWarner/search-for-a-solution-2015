# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150322_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner_email',
            field=models.TextField(default='dave@gmail.com'),
            preserve_default=False,
        ),
    ]

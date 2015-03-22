# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_comment_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 13, 29, 9, 15703), auto_now_add=True),
            preserve_default=False,
        ),
    ]

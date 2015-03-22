# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150321_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

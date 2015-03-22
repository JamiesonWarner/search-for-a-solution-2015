# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_project_owner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner_role',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]

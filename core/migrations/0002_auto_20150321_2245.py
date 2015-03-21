# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='wanted',
            name='tags',
        ),
        migrations.AddField(
            model_name='project',
            name='owner_role',
            field=models.ForeignKey(default=1, to='core.Role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wanted',
            name='role',
            field=models.ForeignKey(default=1, to='core.Role'),
            preserve_default=False,
        ),
    ]

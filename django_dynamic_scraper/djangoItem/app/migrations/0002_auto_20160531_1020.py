# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='excerpt',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='publish_date',
            field=models.DateTimeField(default='', blank=True),
        ),
    ]

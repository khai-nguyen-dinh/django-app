# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160531_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='publish_date',
            field=models.DateTimeField(blank=True),
        ),
    ]

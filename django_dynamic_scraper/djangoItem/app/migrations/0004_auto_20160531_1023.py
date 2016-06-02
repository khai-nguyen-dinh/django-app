# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160531_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='categories',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='publish_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

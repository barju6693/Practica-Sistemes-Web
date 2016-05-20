# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='marca',
            field=models.ForeignKey(default=1, to='icars.Marca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmission',
            name='motor',
            field=models.ForeignKey(default=1, to='icars.Motor'),
            preserve_default=False,
        ),
    ]

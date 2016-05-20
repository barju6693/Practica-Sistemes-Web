# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icars', '0002_auto_20160520_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='marca',
            field=models.ForeignKey(related_name='models', to='icars.Marca', null=True),
        ),
    ]

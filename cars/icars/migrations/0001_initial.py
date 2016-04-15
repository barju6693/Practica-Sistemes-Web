# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estil',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('trim', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('niceName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('niceName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('equipmentType', models.TextField(default=b'ENGINE')),
                ('availability', models.TextField()),
                ('compressionRatio', models.DecimalField(max_digits=7, decimal_places=5)),
                ('cylinder', models.PositiveSmallIntegerField()),
                ('size', models.DecimalField(max_digits=7, decimal_places=4)),
                ('displacement', models.PositiveSmallIntegerField()),
                ('configuration', models.TextField()),
                ('fuelType', models.TextField()),
                ('horsePower', models.PositiveSmallIntegerField()),
                ('torque', models.PositiveSmallIntegerField()),
                ('totalValues', models.PositiveSmallIntegerField()),
                ('manufacturerEngineCode', models.TextField()),
                ('typeN', models.TextField()),
                ('code', models.TextField()),
                ('compressorType', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('equipmentType', models.TextField(default=b'TRANSMISSION')),
                ('availability', models.TextField()),
                ('automaticType', models.TextField()),
                ('transsmisionType', models.TextField()),
                ('numberOfSpeeds', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('year', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]

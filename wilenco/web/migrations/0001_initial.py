# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noSerie', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('potencia', models.CharField(max_length=50)),
                ('capacidad', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to=b'img/productos', blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cotizadorID', models.CharField(max_length=10)),
                ('fechaDeSolicitud', models.DateField()),
                ('nombresCliente', models.CharField(max_length=20)),
                ('apellidosCliente', models.CharField(max_length=20)),
                ('telefonoCliente', models.CharField(max_length=15)),
                ('mailCliente', models.CharField(max_length=50)),
                ('descripcionObra', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='cedulaCliente',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fechaCreada',
            field=models.DateField(auto_now=True),
        ),
    ]

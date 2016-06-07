# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tipo', models.BooleanField(default=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('fechaCreada', models.DateField()),
                ('fechaEscojida', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedulaCliente', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]

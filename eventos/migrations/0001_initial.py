# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tkt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Espacios',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('publicidad', models.ImageField(upload_to='')),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Espacio')),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mombre', models.CharField(max_length=50)),
                ('cantidad_lugares', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Espacio')),
            ],
        ),
        migrations.AddField(
            model_name='lugar',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Sector'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Lugar'),
        ),
    ]

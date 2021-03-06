# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-08 02:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('fechaRealizacion', models.DateField(verbose_name='Fecha a realizar')),
                ('hora', models.TimeField(verbose_name='Hora de Realizacion')),
                ('descripcion', models.TextField(max_length=800)),
                ('imagen', models.ImageField(default='imgActividad/default.jpg', upload_to='imgActividad/')),
                ('fechaPublicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('puntuacion', models.IntegerField(default=0)),
                ('visitas', models.IntegerField(default=0)),
                ('autorizado', models.SmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['-fechaRealizacion'],
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='Capsulas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPublicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('texto', models.TextField(max_length=225)),
                ('autorizado', models.SmallIntegerField(default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'capsula',
                'verbose_name_plural': 'capsulas',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=200)),
                ('fechaComentario', models.DateField(verbose_name='Fecha del comentario')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Actividad')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArtista', models.CharField(max_length=100)),
                ('nombreReal', models.CharField(max_length=65)),
                ('imagen', models.ImageField(default='imgPerfil/default.jpg', upload_to='imgPerfil/')),
                ('sexo', models.SmallIntegerField(default=0)),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaRegistro', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('visitas', models.IntegerField(default=0)),
                ('autorizado', models.SmallIntegerField(default=0)),
                ('categoria', models.ManyToManyField(to='api.Categoria')),
            ],
            options={
                'ordering': ['-fechaRegistro'],
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRol', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'rol',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.AddField(
            model_name='perfil',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rol'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actividad',
            name='categoria',
            field=models.ManyToManyField(to='api.Categoria'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='perfil',
            field=models.ManyToManyField(db_index=True, to='api.Perfil'),
        ),
    ]

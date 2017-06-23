# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-29 10:20
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
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localurl', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('extension', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColP2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n1', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n2', models.CharField(blank=True, max_length=300, null=True)),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Archivo')),
                ('media_n1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n1p2', to='principal.Archivo')),
                ('media_n2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n2p2', to='principal.Archivo')),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField()),
                ('sinVideo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(default=b'', max_length=300)),
                ('transcripcion', models.CharField(blank=True, max_length=10000, null=True)),
                ('urlyt', models.CharField(max_length=100)),
                ('ejercicios', models.ManyToManyField(to='principal.Ejercicio')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Idioma')),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Archivo')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoP1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_f1', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_f2', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n1', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n2', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n3', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n4', models.CharField(blank=True, max_length=300, null=True)),
                ('media_f1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_f1', to='principal.Archivo')),
                ('media_f2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_f2', to='principal.Archivo')),
                ('media_n1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n1', to='principal.Archivo')),
                ('media_n2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n2', to='principal.Archivo')),
                ('media_n3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n3', to='principal.Archivo')),
                ('media_n4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_n4', to='principal.Archivo')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoP2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preg', to='principal.ColP2')),
                ('resps', models.ManyToManyField(blank=True, related_name='resps', to='principal.ColP2')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoP3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(default=0)),
                ('origen', models.CharField(blank=True, max_length=200, null=True)),
                ('opcion1', models.CharField(blank=True, max_length=100, null=True)),
                ('opcion2', models.CharField(blank=True, max_length=100, null=True)),
                ('texto_n1', models.CharField(blank=True, max_length=300, null=True)),
                ('texto_n2', models.CharField(blank=True, max_length=300, null=True)),
                ('audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='principal.Archivo')),
                ('media_n1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hint1', to='principal.Archivo')),
                ('media_n2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hint2', to='principal.Archivo')),
            ],
        ),
        migrations.AddField(
            model_name='recursop3',
            name='textos',
            field=models.ManyToManyField(blank=True, related_name='textop3', to='principal.Texto'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Tema'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='recursosP1',
            field=models.ManyToManyField(blank=True, to='principal.RecursoP1'),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='recursosP2',
            field=models.ManyToManyField(blank=True, to='principal.RecursoP2'),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='recursosP3',
            field=models.ManyToManyField(blank=True, to='principal.RecursoP3'),
        ),
    ]

# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

import os

PROJECT_PATH = os.path.dirname("__file__")


class Archivo(models.Model):
    localurl = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    extension = models.CharField(max_length=5)
    nombre = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.localurl


class RecursoP1(models.Model):
    texto_f1 = models.CharField(max_length=300, null=True, blank=True)
    texto_f2 = models.CharField(max_length=300, null=True, blank=True)

    media_f1 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_f1')
    media_f2 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_f2')

    texto_n1 = models.CharField(max_length=300, null=True, blank=True)
    texto_n2 = models.CharField(max_length=300, null=True, blank=True)
    texto_n3 = models.CharField(max_length=300, null=True, blank=True)
    texto_n4 = models.CharField(max_length=300, null=True, blank=True)

    media_n1 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n1')
    media_n2 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n2')
    media_n3 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n3')
    media_n4 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n4')

    def __unicode__(self):
        return "%s" % self.id


class ColP2(models.Model):
    texto = models.CharField(max_length=300, null=True, blank=True)
    media = models.ForeignKey(Archivo, null=True, blank=True)

    texto_n1 = models.CharField(max_length=300, null=True, blank=True)
    texto_n2 = models.CharField(max_length=300, null=True, blank=True)

    media_n1 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n1p2')
    media_n2 = models.ForeignKey(Archivo, null=True, blank=True, related_name='media_n2p2')

    def __unicode__(self):
        return u"%s_%s" % (self.id, self.texto)


class RecursoP2(models.Model):
    preg = models.ForeignKey(ColP2, related_name='preg', null=True, blank=True)
    resps = models.ManyToManyField(ColP2, related_name='resps', blank=True)

    def __unicode__(self):
        return "%s" % self.id

class Texto(models.Model):
    # tipos: 1-texto plano, 2-audio, 3-fill, 4-opciones, 5-drag'n drop
    tipo = models.IntegerField(default=0)
    origen = models.CharField(max_length=200, null=True, blank=True)
    audio = models.ForeignKey(Archivo, null=True, blank=True, related_name='audio')

    opcion1 = models.CharField(max_length=100, null=True, blank=True)
    opcion2 = models.CharField(max_length=100, null=True, blank=True)

    texto_n1 = models.CharField(max_length=300, null=True, blank=True)
    texto_n2 = models.CharField(max_length=300, null=True, blank=True)

    media_n1 = models.ForeignKey(Archivo, null=True, blank=True, related_name='hint1')
    media_n2 = models.ForeignKey(Archivo, null=True, blank=True, related_name='hint2')

    def __unicode__(self):
        return u"%s_%s" % (self.origen, self.id)


class RecursoP3(models.Model):
    textos = models.ManyToManyField(Texto, related_name='textop3', blank=True)

    def __unicode__(self):
        return "%s" % self.id

class Ejercicio(models.Model):
    tipo = models.IntegerField()
    sinVideo = models.IntegerField(default=0)
    recursosP1 = models.ManyToManyField(RecursoP1, blank=True)
    recursosP2 = models.ManyToManyField(RecursoP2, blank=True)
    recursosP3 = models.ManyToManyField(RecursoP3, blank=True)
    posicion = models.IntegerField(default=1)

    class Meta:
        ordering = ['posicion']

    def __unicode__(self):
        return u"%s_%s" % (self.tipo, self.id)


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.nombre


class Nivel(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.nombre


class Tema(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, default='')
    usuario = models.ForeignKey(User)
    media = models.ForeignKey(Archivo, null=True, blank=True)
    transcripcion = models.CharField(max_length=10000, null=True, blank=True)
    ejercicios = models.ManyToManyField(Ejercicio)
    idioma = models.ForeignKey(Idioma)
    nivel = models.ForeignKey(Nivel)
    tema = models.ForeignKey(Tema)
    urlyt = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return u"%s_%s" % (self.usuario.username, self.nombre)

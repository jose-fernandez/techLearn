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

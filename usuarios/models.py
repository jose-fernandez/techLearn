# -*- encoding: utf-8 -*-

import os

from django.contrib.auth.models import User
from django.db import models

PROJECT_PATH = os.path.dirname("__file__")


class Tokenregister(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.token


class TokenRecuperarPass(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.token

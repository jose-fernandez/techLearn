# -*- coding: utf-8 -*-
from settings import *

EXTRA_MIDDLEWARE_CLASSES = (

)

EXTRA_INSTALLED_APPS = (

)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'dbsqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# -*- coding: utf-8 -*-

"""
Django settings for configuracion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import django.conf.global_settings
from django.utils.translation import ugettext_lazy as tl
from django.utils.translation import activate
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(__file__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o777

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pfer@di&c5s#o!_o!me@(sjd*i%t4)8s_wb0hs7m@mgl-)xw0%4zon'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (

    'django.contrib.staticfiles',
    'jet',  
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'mathfilters',
    'floppyforms',
    'bootstrapform',
    'usuarios',
    'principal',
)
INSTALLED_APPS_MIGRATE = (

    'usuarios',
    'principal',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


"""
para poder instalar con apache hay que descomentar static root y comentar
los staticfiles_dirs hacer python manage.py collectstatic y dejar comoe staba
"""
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.request',
                'configuracion.processors.comun',
            ],
        },
    },
]

LANGUAGES = (
    ('es', tl('Spanish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

ROOT_URLCONF = 'configuracion.urls'

WSGI_APPLICATION = 'configuracion.wsgi.application'

LANGUAGE_CODE = 'es-es'

SESSION_COOKIE_AGE = 18000 #seg
SESSION_SAVE_EVERY_REQUEST = True

SITE_ID = 1

TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
MEDIA_URL = 'static/media/'

MEDIA_FILES = MEDIA_ROOT + '/archivos'
MEDIA_FILES_URL = MEDIA_URL + 'archivos/'

MEDIA_VIDEO = MEDIA_ROOT + '/video'
MEDIA_VIDEO_URL = MEDIA_URL+'video/'

MEDIA_AUDIO = MEDIA_ROOT + '/audios'
MEDIA_AUDIO_URL = MEDIA_URL +'audios/'

MEDIA_IMAGE = MEDIA_ROOT + '/imagenes'
MEDIA_IMAGE_URL = MEDIA_URL +'imagenes/'


GALERIA_ROOT = MEDIA_ROOT + '/galeria'
GALERIA_URL = MEDIA_URL + 'galeria/'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/principal/inicio/'

# Add to your settings file
CONTENT_TYPES = ['image', 'video', 'audio']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "5242880"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

try:
    from configuracion import local_settings
except ImportError as e:
    print (e.message, type(e))
    print ("""
    -------------------------------------------------------------------------
    You need to create a local_settings.py file which needs to contain at least
    database connection information.
    -------------------------------------------------------------------------
    """)
    import sys
    sys.exit(1)
else:
  # Import any symbols that begin with A-Z. Append to lists any symbols that
  # begin with "EXTRA_".
  import re
  for attr in dir(local_settings):
    match = re.search('^EXTRA_(\w+)', attr)
    if match:
      name = match.group(1)
      value = getattr(local_settings, attr)
      try:
        globals()[name] += value
      except KeyError:
        globals()[name] = value
    elif re.search('^[A-Z]', attr):
      globals()[attr] = getattr(local_settings, attr)


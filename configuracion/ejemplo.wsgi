import os, sys

sys.path.append('/home/brian/git/Django')
sys.path.append('/home/brian/git/Django/selan')
sys.path.insert(0,os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))

os.environ['DJANGO_SETTINGS_MODULE']="configuracion.settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()



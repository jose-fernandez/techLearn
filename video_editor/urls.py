from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from video_editor import views

urlpatterns = patterns('',
                        url(r'^descargar$', views.descargarVideoYT, name='descargarYT'),
                        url(r'^cargarVideo$', views.cargarVideo, name='cargarVideo'),

                       )

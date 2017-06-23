from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from usuarios import views

urlpatterns = patterns('',


                       url(r'^crear/$', login_required(views.UsuarioCreate.as_view()), name='usuario_create'),
                       url(r'^perfil/(?P<pk>\d+)$', login_required(views.UsuarioPerfil.as_view()),
                           name='usuario_perfil'),
                       url(r'^editar/(?P<pk>\d+)$', login_required(views.UsuarioEdit.as_view()), name='usuario_edit'),
                       url(r'^borrar/(?P<pk>\d+)$', login_required(views.UsuarioDelete.as_view()),
                           name='usuario_delete'),

                       url(r'^recuperarpass/$', views.UsuarioRecuperarContrasena.as_view(),
                           name='recuperar_contrasena'),

                       )

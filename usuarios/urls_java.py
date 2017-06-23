# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

urlpatterns = patterns('', url(r'^login/$', 'usuarios.views_java.login'),
                       url(r'^logout/$', 'usuarios.views_java.logout'),
                       url(r'^get_perfil/$', 'usuarios.views_java.get_perfil'),
                       url(r'^comprobar_token/$', 'usuarios.views_java.comprobar_token'),

                       url(r'^recuperar_pass/$', 'usuarios.views_java.recuperar_pass'),

                       )

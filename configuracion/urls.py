# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns


from django.contrib import admin
admin.autodiscover()


urlpatterns = i18n_patterns(
    url(r'^$', 'configuracion.views.inicio', name='inicio'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}, name='logout'),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^usuarios/java/', include('usuarios.urls_java')),
    url(r'^principal/', include('principal.urls')),
    url(r'^editor/', include('video_editor.urls')),
    url(r'^p3_temp/(?P<pk>\d+)$', 'configuracion.views.p3_temp', name='p3_temp'),
    url(r'^selector/(?P<pk>\d+)$', 'configuracion.views.selector', name='selector'),
    url(r'^view/(?P<pk>\d+)$', 'configuracion.views.proyecto_view', name='proyecto_view'),

    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
)

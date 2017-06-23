# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag(name='get_nombre_archivo')
def get_nombre_archivo(url):

    u = url.split('/')[-1]

    return u

@register.simple_tag(name='get_tipo_archivo')
def get_tipo_archivo(url):

    u = url.split('/')[-1]
    exten = u.split('.')[-1]
    return exten

@register.simple_tag(name='get_url_server_galeria')
def get_url_server(url):

    cortes = url.find("/galeria")+1
    urlfinal = url[0:cortes]
    return urlfinal

@register.simple_tag(name='get_url_server_mensajes')
def get_url_server(url):

    cortes = url.find("/mensajes")+1
    urlfinal = url[0:cortes]
    return urlfinal
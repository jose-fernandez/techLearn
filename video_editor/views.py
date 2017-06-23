# -*- encoding: utf-8 -*-
import json
import os
import sys
import uuid
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pytube import YouTube

from configuracion import settings
from principal import models

# funcion extra a implementar debido a su estado incompleto.
def crearArchivo(afile):
    url = settings.MEDIA_FILES_URL

    dpath = settings.MEDIA_FILES

    os.system("mkdir " + dpath)
    os.system("chmod -R 777" + dpath)
    nombre = afile.name
    nombre = nombre.replace(" ", "_")
    lpath = dpath + "/" + nombre

    destination = open(lpath, 'wb+')
    for chunk in afile.chunks():
        destination.write(chunk)
    destination.close()

    u = lpath.split('/')[-1]
    exten = u.split('.')[-1]
    exten = exten.lower()

    url = url + nombre
    archivo = models.Archivo(url=url, localurl=lpath, extension=exten, nombre=nombre)
    archivo.save()

    return archivo

@csrf_exempt
def cargarVideo(request):
    response_data = {}
    if request.FILES and request.FILES.get('file_upload'):
        file = crearArchivo(request.FILES.get('file_upload'))

        if file.extension == 'mp4' or file.extension == 'ogg' or file.extension == 'webm':
            response_data['result'] = 'ok'
            response_data['url'] = file.url
            response_data['ext'] = file.extension
        else:
            response_data['result'] = 'error'
            response_data['msg'] = 'ext'

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def descargarVideoYT(request):
    response_data = {}
    url = request.POST.get('urlyt')
    yt = YouTube(url)

    video = yt.get('mp4', '720p')

    dpath = settings.MEDIA_FILES
    nombre = str(uuid.uuid4())+".mp4"
    
    lpath = dpath + "/" + nombre

    try:
        video.download(lpath)
        response_data['result'] = 'ok'
        response_data['url'] = settings.MEDIA_FILES_URL + nombre

    except Exception as e:
        response_data['result'] = 'error'
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


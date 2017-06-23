# -*- encoding: utf-8 -*-
import os
import traceback

from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
import django.http as http
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from annoying.functions import get_object_or_None
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import FormView, DeleteView, CreateView
from django.http import HttpResponse
from configuracion import settings
from principal import forms, models
from django.core import serializers
from principal.models import Proyecto
import json


class ProyectoCreate(CreateView):
    model = Proyecto
    template_name = 'proyectos/proyectos_create.html'
    form_class = forms.ProyectoForm

    def get(self, request, *args, **kwargs):
        proyectoform = forms.ProyectoForm(initial=self.initial)
        return render(request, self.template_name, {'proyectoform': proyectoform})

    def post(self, request, *args, **kwargs):
        data = request
        proyectoform = forms.ProyectoForm(data.POST)

        if proyectoform.is_valid():

            proyecto = proyectoform.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()

            file_list = request.FILES.getlist('media')

            for afile in file_list:

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

                url = url + "/" + nombre
                archivo = models.Archivo(url=url, localurl=lpath, extension=exten, nombre=nombre)
                archivo.save()
                proyecto.media = archivo
                proyecto.save()

            return http.HttpResponseRedirect(reverse('selector', kwargs={'pk': proyecto.id}))
        return render(request, self.template_name, {'proyectoform': proyectoform})


class ProyectosList(CreateView):
    template_name = 'proyectos/proyectos_list.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        by_id = models.Proyecto.objects.filter(usuario=user).order_by('id')
        return render(request, self.template_name, {'user': user, 'proyectos': by_id})


class ProyectoDelete(DeleteView):
    template_name = 'proyectos/proyecto_delete.html'
    form_class = forms.ContrasenaForm

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        proyecto = get_object_or_404(models.Proyecto, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'proyecto': proyecto, 'form': form})

    def post(self, request, *args, **kwargs):
        proyecto = get_object_or_404(models.Proyecto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            if proyecto.pk != 0:
                proyecto.delete()
                return http.HttpResponseRedirect(reverse('proyecto_list'))
            else:
                return http.HttpResponseRedirect(reverse('proyecto_list'))

        else:
            return render(request, self.template_name, {'proyecto': proyecto, 'form': form})


class ProyectoEdit(FormView):
    template_name = 'proyectos/project_edit.html'
    form_class = forms.ProyectoForm

    def get(self, request, *args, **kwargs):
        proyecto = get_object_or_404(models.Proyecto, pk=self.kwargs['pk'])
        proyectoform = self.form_class(
            initial={'transcripcion': proyecto.transcripcion, 'descripcion': proyecto.descripcion,
                     'tema': proyecto.tema, 'idioma': proyecto.idioma, 'nivel': proyecto.nivel,
                     'nombre': proyecto.nombre, 'urlyt': proyecto.urlyt})
        return render(request, self.template_name, {'proyectoform': proyectoform, 'proyecto': proyecto})

    def post(self, request, *args, **kwargs):
        proyecto = get_object_or_404(models.Proyecto, pk=self.kwargs['pk'])
        proyectoform = forms.ProyectoForm(request.POST or None, instance=proyecto)

        if proyectoform.is_valid():
            file_list = request.FILES.getlist('media')

            for afile in file_list:
                proyecto.media = crearArchivo(afile)
                proyecto.save()

            proyectoform.save()

            return http.HttpResponseRedirect(reverse('proyecto_view', kwargs={'pk': proyecto.id}))

        return render(request, self.template_name, {'proyetoform': proyectoform, 'proyecto': proyecto})


def Del_ejercicio(request, pk, pk2):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk2)
    proyecto = get_object_or_404(models.Proyecto, pk=pk)
    ejs = proyecto.ejercicios.all()
    for ej in ejs:
        if ej.posicion > ejercicio.posicion:
            ej.posicion -=1
            ej.save()
    proyecto.ejercicios.remove(ejercicio)
    # ejercicio.recursos.all().delete()
    ejercicio.delete()
    return http.HttpResponseRedirect(reverse('proyecto_view', kwargs={'pk': proyecto.id}))


def del_recurso(request, pk, pk2, pk3):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk2)
    proyecto = get_object_or_404(models.Proyecto, pk=pk3)

    if ejercicio.tipo == 3:
        recurso = get_object_or_404(models.RecursoP3, pk=pk)
        ejercicio.recursosP3.remove(recurso)
        ejercicio.save()

        return http.HttpResponseRedirect(reverse('creando_ej3', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))

    if ejercicio.tipo == 2:
        recurso = get_object_or_404(models.RecursoP2, pk=pk)
        ejercicio.recursosP2.remove(recurso)
        ejercicio.save()

        return http.HttpResponseRedirect(reverse('creando_ej2', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))

    if ejercicio.tipo == 1:
        recurso = get_object_or_404(models.RecursoP1, pk=pk)
        ejercicio.recursosP1.remove(recurso)
        ejercicio.save()

        return http.HttpResponseRedirect(reverse('creando_ej', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))


def crearEjercicio(request, pk, pk2):
    proyecto = get_object_or_404(models.Proyecto, pk=pk)
    ejercicio = models.Ejercicio(tipo=pk2)
    ejercicio.save()

    if pk2 == '1':
        return http.HttpResponseRedirect(reverse('creando_ej', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))
    elif pk2 == '2':
        return http.HttpResponseRedirect(reverse('creando_ej2', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))
    elif pk2 == '3':
        return http.HttpResponseRedirect(reverse('creando_ej3', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))

def creandoEj3(request, pk, pk2):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)
    proyecto = get_object_or_404(models.Proyecto, pk=pk2)
    return render_to_response('proyectos/creadores/maker_temp3.html',
                              context_instance=RequestContext(request, {'ejercicio': ejercicio, 'proyecto': proyecto}))


def guardarEjercicio(request, pk, pk2):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)

    proyecto = get_object_or_404(models.Proyecto, pk=pk2)
    proyecto.ejercicios.add(ejercicio)
    proyecto.save()
    return render_to_response('proyectos/proyect_view.html',
                              context_instance=RequestContext(request, {'proyecto': proyecto}))


def guardarRecursoP1(request):
    ejercicio = get_object_or_404(models.Ejercicio, pk=request.POST['ide'])
    proyecto = get_object_or_404(models.Proyecto, pk=request.POST['idp'])
    recurso = models.RecursoP1()
    recurso.texto_f1 = request.POST['texto_f1']
    recurso.texto_f2 = request.POST['texto_f2']

    recurso.texto_n1 = request.POST['texto_n1']
    recurso.texto_n2 = request.POST['texto_n2']
    recurso.texto_n3 = request.POST['texto_n3']
    recurso.texto_n4 = request.POST['texto_n4']

    recurso.save()
    media_f1_list = request.FILES.getlist('media_f1')
    media_f2_list = request.FILES.getlist('media_f2')

    media_n1_list = request.FILES.getlist('media_n1')
    media_n2_list = request.FILES.getlist('media_n2')
    media_n3_list = request.FILES.getlist('media_n3')
    media_n4_list = request.FILES.getlist('media_n4')

    for afile in media_f1_list:
        recurso.media_f1 = crearArchivo(afile)

    for afile in media_f2_list:
        recurso.media_f2 = crearArchivo(afile)

    for afile in media_n1_list:
        recurso.media_n1 = crearArchivo(afile)

    for afile in media_n2_list:
        recurso.media_n2 = crearArchivo(afile)

    for afile in media_n3_list:
        recurso.media_n3 = crearArchivo(afile)

    for afile in media_n4_list:
        recurso.media_n4 = crearArchivo(afile)

    recurso.save()
    ejercicio.recursosP1.add(recurso)

    return http.HttpResponseRedirect(reverse('creando_ej', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))


def guardarRecursoP2(request):
    ejercicio = get_object_or_404(models.Ejercicio, pk=request.POST['ide'])
    proyecto = get_object_or_404(models.Proyecto, pk=request.POST['idp'])
    recurso = get_object_or_404(models.RecursoP2, pk=request.POST['idr'])
    col = models.ColP2()
    col.save()

    col.texto = request.POST['texto']
    col.texto_n1 = request.POST['texto_n1']
    col.texto_n2 = request.POST['texto_n2']
    col.save()

    media_list = request.FILES.getlist('media')
    media_n1_list = request.FILES.getlist('media_n1')
    media_n2_list = request.FILES.getlist('media_n2')

    for afile in media_list:
        col.media = crearArchivo(afile)

    for afile in media_n1_list:
        col.media_n1 = crearArchivo(afile)

    for afile in media_n2_list:
        col.media_n2 = crearArchivo(afile)
    col.save()

    recurso.preg = col
    recurso.save()

    ejercicio.recursosP2.add(recurso)

    return http.HttpResponseRedirect(reverse('creando_ej2', kwargs={'pk': ejercicio.id, 'pk2': proyecto.id}))


def creandoRecurso(request, pk, pk2):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)
    proyecto = get_object_or_404(models.Proyecto, pk=pk2)
    return render_to_response('proyectos/creadores/crear_recurso.html',
                              context_instance=RequestContext(request, {'id': ejercicio.id, 'idp': proyecto.id}))


def creandoRecurso2_redirect(request, pk, pk2, pk3):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)
    proyecto = get_object_or_404(models.Proyecto, pk=pk2)
    recurso = get_object_or_404(models.RecursoP2, pk=pk3)
    return render_to_response('proyectos/creadores/crear_recursoP2.html', context_instance=RequestContext(request,
                                                                                                          {
                                                                                                              'ejercicio': ejercicio,
                                                                                                              'idp': proyecto.id,

                                                                                                              'recurso': recurso}))


def creandoRecurso2(request, pk, pk2):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)
    proyecto = get_object_or_404(models.Proyecto, pk=pk2)
    recurso = models.RecursoP2()
    recurso.save()
    return render_to_response('proyectos/creadores/crear_recursoP2.html', context_instance=RequestContext(request,
                                                                                                          {
                                                                                                              'ejercicio': ejercicio,
                                                                                                              'idp': proyecto.id,
                                                                                                              'recurso': recurso}))


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


def do_project(request, pk):
    proyecto = get_object_or_404(models.Proyecto, pk=pk)
    return render_to_response('proyectos/doProyect.html',
                              context_instance=RequestContext(request, {'proyecto': proyecto}))


def video_editor(request):
    return render_to_response('video_editor.html',
                              context_instance=RequestContext(request))


def buscar(request):
    idiomas = serializers.serialize("python", models.Idioma.objects.all(), fields=('nombre'))
    niveles = serializers.serialize("python", models.Nivel.objects.all(), fields=('nombre'))
    temas = serializers.serialize("python", models.Tema.objects.all(), fields=('nombre'))
    return render_to_response('proyectos/buscador.html',
                              context_instance=RequestContext(request,
                                                              {'idiomas': idiomas, 'niveles': niveles, 'temas': temas}))


# -------------------------------------------------------------------------Ajax
@csrf_exempt
def crearRespuesta(request):
    recurso = get_object_or_404(models.RecursoP2, pk=request.POST.get('idr'))
    col = models.ColP2()
    col.save()
    response_data = {}
    if request.FILES and request.FILES.get('media'):
        file = crearArchivo(request.FILES.get('media'))
        col.media = file
        col.save()
        response_data['media'] = file.url

    if request.FILES and request.FILES.get('media1'):
        file = crearArchivo(request.FILES.get('media1'))
        col.media_n1 = file
        col.save()

    if request.FILES and request.FILES.get('media2'):
        file = crearArchivo(request.FILES.get('media2'))
        col.media_n2 = file
        col.save()

    try:
        if request.POST.get('hint1'):
            col.texto_n1 = request.POST.get('hint1')
            col.save()
    except KeyError:
        print ('error')

    try:
        if request.POST.get('texto'):
            col.texto = request.POST.get('texto')
            col.save()
            response_data['texto'] = col.texto
    except KeyError:
        print ('error')

    try:
        if request.POST.get('hint2'):
            col.texto_n2 = request.POST.get('hint2')
            col.save()
    except KeyError:
        print ('error')
    col.save()

    recurso.resps.add(col)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearRecursoP3(request):
    response_data = {}
    jsondata = json.loads(request.body)
    ides = jsondata.get('array')
    rec = models.RecursoP3()
    rec.save()
    ejer = get_object_or_404(models.Ejercicio, pk=ides[0])
    ides.pop(0)
    for idd in ides:
        text = get_object_or_404(models.Texto, pk=idd)
        rec.textos.add(text)
        rec.save()
        ejer.recursosP3.add(rec)
        ejer.save()

    response_data['key'] = rec.pk

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearPalabra(request):
    pal = models.Texto(origen=request.POST['texto'], tipo=1)
    pal.save()
    response_data = {}
    response_data['result'] = 'Create post successful!'
    response_data['palpk'] = pal.pk
    response_data['texto'] = pal.origen
    response_data['key'] = pal.pk

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def guardarArchivo(request):
    response_data = {}
    if request.FILES and request.FILES.get('file_upload'):
        file = crearArchivo(request.FILES.get('file_upload'))
        pal = models.Texto(audio=file, tipo=2)
        pal.save()
        response_data['result'] = 'Create post successful!'
        response_data['url'] = file.url
        response_data['ext'] = file.extension
        response_data['key'] = pal.pk

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearFill(request):
    pal = models.Texto(origen=request.POST['texto'], tipo=3)
    pal.save()
    response_data = {}
    response_data['result'] = 'Create post successful!'
    response_data['key'] = pal.pk
    response_data['texto'] = pal.origen

    if request.FILES and request.FILES.get('media1'):
        file = crearArchivo(request.FILES.get('media1'))
        pal.media_n1 = file
        pal.save()

    if request.FILES and request.FILES.get('media2'):
        file = crearArchivo(request.FILES.get('media2'))
        pal.media_n2 = file
        pal.save()
    try:
        if request.POST['hint1']:
            pal.texto_n1 = request.POST['hint1']
            pal.save()
    except KeyError:
        print ('error')

    try:
        if request.POST['hint2']:
            pal.texto_n2 = request.POST['hint2']
            pal.save()
    except KeyError:
        print ('error')

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearOptions(request):
    pal = models.Texto(origen=request.POST['texto'], opcion1=request.POST['opcion2'], opcion2=request.POST['opcion3'],
                       tipo=4)
    pal.save()
    response_data = {}
    response_data['result'] = 'Create post successful!'
    response_data['key'] = pal.pk
    response_data['texto'] = pal.origen
    response_data['op2'] = pal.opcion1
    response_data['op3'] = pal.opcion2

    if request.FILES and request.FILES.get('media1'):
        file = crearArchivo(request.FILES.get('media1'))
        pal.media_n1 = file
        pal.save()

    if request.FILES and request.FILES.get('media2'):
        file = crearArchivo(request.FILES.get('media2'))
        pal.media_n2 = file
        pal.save()
    try:
        if request.POST.get('hint1'):
            pal.texto_n1 = request.POST.get('hint1')
            pal.save()
    except KeyError:
        print ('error h1')
        traceback.print_exc()

    try:
        if request.POST['hint2']:
            pal.texto_n2 = request.POST['hint2']
            pal.save()
    except KeyError:
        print ('error h2')
        traceback.print_exc()

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearDrag(request):
    pal = models.Texto(origen=request.POST['texto'], tipo=5)
    pal.save()
    response_data = {}
    response_data['result'] = 'Create post successful!'
    response_data['key'] = pal.pk
    response_data['texto'] = pal.origen

    if request.FILES and request.FILES.get('media1'):
        file = crearArchivo(request.FILES.get('media1'))
        pal.media_n1 = file
        pal.save()

    if request.FILES and request.FILES.get('media2'):
        file = crearArchivo(request.FILES.get('media2'))
        pal.media_n2 = file
        pal.save()
    try:
        if request.POST['hint1']:
            pal.texto_n1 = request.POST['hint1']
            pal.save()
    except KeyError:
        print ('error')

    try:
        if request.POST['hint2']:
            pal.texto_n2 = request.POST['hint2']
            pal.save()
    except KeyError:
        print ('error')

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def crearSalto(request):
    pal = models.Texto(origen="salto", tipo=6)
    pal.save()
    response_data = {}
    response_data['result'] = 'ok'
    response_data['palpk'] = pal.pk
    response_data['texto'] = pal.origen
    response_data['key'] = pal.pk

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def buscar_unidades(request):
    nombre = request.POST.get('nombre')
    filter_dict = {'nombre__contains': nombre}

    idioma_n = request.POST.get('idioma')
    if idioma_n != 'Todo':
        idioma = get_object_or_None(models.Idioma, nombre=idioma_n)
        filter_dict['idioma'] = idioma

    nivel_n = request.POST.get('nivel')
    if nivel_n != 'Todo':
        nivel = get_object_or_None(models.Nivel, nombre=nivel_n)
        filter_dict['nivel'] = nivel

    tema_n = request.POST.get('tema')
    if tema_n != 'Todo':
        tema = get_object_or_None(models.Tema, nombre=tema_n)
        filter_dict['tema'] = tema

    lista = Proyecto.objects.filter(**filter_dict).order_by('-id')

    response_data = {'result': 'ok', 'lista': []}

    for a in lista:
        try:
            response_data['lista'].append(
                {'usuario': str(a.usuario.get_username()), 'id_proyecto': a.pk, 'media': a.media.url,
                 'descripcion': a.descripcion, 'idioma': a.idioma.nombre, 'nivel': a.nivel.nombre,
                 'tema': a.tema.nombre, 'nombre': a.nombre})
        except Exception:
            response_data['lista'].append(
                {'usuario': str(a.usuario.get_username()), 'id_proyecto': a.pk, 'descripcion': a.descripcion,
                 'idioma': a.idioma.nombre, 'nivel': a.nivel.nombre, 'tema': a.tema.nombre, 'nombre': a.nombre})

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def checkEjericio(request):
    ej = get_object_or_None(models.Ejercicio, pk=request.POST.get('ejercicio'))
    check = request.POST.get('checked')
    if check == '1':
        ej.sinVideo = 1
    else:
        ej.sinVideo = 0
    ej.save()
    response_data = {}
    response_data['result'] = 'ok'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def setPosicion(request):
    ej = get_object_or_None(models.Ejercicio, pk=request.POST.get('ejercicio'))
    proyecto = get_object_or_None(models.Proyecto, pk=request.POST.get('proyecto'))
    ejs = proyecto.ejercicios.all()

    n_pos = int(request.POST.get('pos'))
    prev_pos = ej.posicion

    if prev_pos > n_pos:
        for eje in ejs:
            if eje.posicion >= n_pos and eje.posicion<prev_pos:
                eje.posicion +=1
                eje.save()

    elif prev_pos < n_pos:
        for eje in ejs:
            if eje.posicion <= n_pos and eje.posicion>prev_pos:
                eje.posicion -=1
                eje.save()

    pos = request.POST.get('pos')
    ej.posicion = pos
    ej.save()
    response_data = {}
    response_data['result'] = 'ok'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def delRecP3(request):
    ej = get_object_or_None(models.Ejercicio, pk=request.POST.get('ejercicio'))
    rec = get_object_or_None(models.RecursoP3, pk=request.POST.get('recurso'))
    ej.recursosP3.remove(rec)
 
    ej.save()
    response_data = {}
    response_data['result'] = 'ok'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

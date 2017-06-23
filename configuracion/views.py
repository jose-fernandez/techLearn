# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from principal import models
from django.template import Context, loader
from django.http import HttpResponse

from django.utils.translation import activate

@login_required()
def inicio(request):
    usuario = request.user
    return render_to_response('principal.html',context_instance=RequestContext(request,{'usuario':usuario}))

def p3_temp(request,pk):
    ejercicio = get_object_or_404(models.Ejercicio, pk=pk)
    return render_to_response('proyectos/p3_temp.html', context_instance=RequestContext(request,{'ejercicio':ejercicio}))

def selector(request,pk):
    proyecto = get_object_or_404(models.Proyecto, pk=pk)
    return render_to_response('proyectos/template_selector.html', context_instance=RequestContext(request,{'proyecto':proyecto}))


def proyecto_view(request,pk):
    proyecto = get_object_or_404(models.Proyecto, pk=pk)
    return render_to_response('proyectos/proyect_view.html', context_instance=RequestContext(request,{'proyecto':proyecto}))
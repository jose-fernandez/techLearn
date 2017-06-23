from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from principal import views

urlpatterns = patterns('',
   url(r'^crearProyecto/$', login_required(views.ProyectoCreate.as_view()), name='proyecto_create'),
   url(r'^listaProyectos/$', login_required(views.ProyectosList.as_view()), name='proyecto_list'),
   url(r'^editProyecto/(?P<pk>\d+)$', login_required(views.ProyectoEdit.as_view()),
       name='proyecto_edit'),
   url(r'^borrarProyecto/(?P<pk>\d+)$', login_required(views.ProyectoDelete.as_view()),
       name='proyecto_delete'),
   url(r'^eliminarEjercicio/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.Del_ejercicio),
       name='del_ejercicio'),
   url(r'^doProject/(?P<pk>\d+)$', views.do_project, name='do_project'),

   url(r'^inicio/$', login_required(views.ProyectosList.as_view()), name='inicio'),
   url(r'^cr_plantilla/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.crearEjercicio),
       name='nuevo_ejercicio'),
   url(r'^creandoEj3/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.creandoEj3),
       name='creando_ej3'),
   url(r'^guardarEj/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.guardarEjercicio),
       name='guardar'),
   url(r'^guardarRecP1//$', login_required(views.guardarRecursoP1), name='guardar_recurso'),
   url(r'^guardarRecP2/$', login_required(views.guardarRecursoP2), name='guardar_recursop2'),

   url(r'^creandoRecurso/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.creandoRecurso),
       name='creando_recurso'),
   url(r'^creandoRecurso2/(?P<pk>\d+)/(?P<pk2>\d+)$', login_required(views.creandoRecurso2),
       name='creando_recurso2'),
   url(r'^creandoRecurso2_r/(?P<pk>\d+)/(?P<pk2>\d+)/(?P<pk3>\d+)$',
       login_required(views.creandoRecurso2_redirect), name='creando_recurso2_redirect'),
   url(r'^crearRecursoP3$', views.crearRecursoP3, name='crear_recursop3'),
   url(r'^delRecurso/(?P<pk>\d+)/(?P<pk2>\d+)/(?P<pk3>\d+)$', login_required(views.del_recurso),
       name='del_recurso'),

   url(r'^crearPalabra$', views.crearPalabra, name='crear_palabra'),
   url(r'^crearSalto$', views.crearSalto, name='crear_salto'),
   url(r'^guardarArchivo$', views.guardarArchivo, name='guardar_archivo'),
   url(r'^guardarFill$', views.crearFill, name='guardar_fill'),
   url(r'^guardarDrag$', views.crearDrag, name='guardar_drag'),
   url(r'^guardarOptions$', views.crearOptions, name='guardar_options'),

   url(r'^crearRespuesta$', views.crearRespuesta, name='crear_respuesta'),

   url(r'^veditor$', views.video_editor, name='veditor'),
   url(r'^buscarUnidades$', views.buscar_unidades, name='accion_buscar'),
   url(r'^checkEjercicio', views.checkEjericio, name='check_ejercicio'),
   url(r'^setPosicion', views.setPosicion, name='set_posicion'),
   url(r'^delrecP3', views.delRecP3, name='del_recursop3'),
)

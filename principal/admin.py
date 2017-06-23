from django.contrib import admin

from principal.models import Proyecto, Idioma, Ejercicio, Nivel, Tema, Archivo, Texto, RecursoP1, \
    RecursoP2, ColP2, RecursoP3

admin.site.register(Proyecto)
admin.site.register(Idioma)
admin.site.register(Ejercicio)
admin.site.register(Nivel)
admin.site.register(Tema)
admin.site.register(RecursoP1)
admin.site.register(RecursoP2)
admin.site.register(Archivo)
admin.site.register(Texto)
admin.site.register(ColP2)
admin.site.register(RecursoP3)

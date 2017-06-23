# -*- encoding: utf-8 -*-

__author__ = 'jFernandez'

import floppyforms as forms

from principal.models import Proyecto, Texto, RecursoP1, Ejercicio
from utilidades import multiplefiles


class ProyectoForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'
    media = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)

    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion", "transcripcion", "idioma", "nivel", "tema","urlyt"]
        widgets = {
            'nombre': forms.TextInput,
            "transcripcion": forms.Textarea,
        }
        exclude = {
            'usuario',
            'media',
            'ejercicios',
        }


class ContrasenaForm(forms.Form):
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')


class EjercicioForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = Ejercicio
        fields = ["recursosP1"]


class RecursoForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'
    media_f1 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)
    media_f2 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)

    media_n1 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)
    media_n2 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)
    media_n3 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)
    media_n4 = multiplefiles.MultiFileField(max_num=1, min_num=0, maximum_file_size=1024 * 1024 * 50)

    class Meta:
        model = RecursoP1
        fields = ["texto_f1", "texto_f2", "media_f1", "media_f2", "texto_n1", "texto_n2", "texto_n3", "texto_n4",
                  "media_n1", "media_n2", "media_n3", "media_n4"]
        widgets = {
            'texto_f1': forms.TextInput
        }
        exclude = {
            "media_f1", "media_f2", "media_n1", "media_n2", "media_n3", "media_n4"
        }


class PalabrasForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = Texto
        fields = ["origen"]
        widgets = {
            'Idioma Origen': forms.CharField(),
        }


class DiccionarioForm(forms.Form):
    error_css_class = 'alert alert-danger'
    palabras = forms.ModelMultipleChoiceField(queryset=Texto.objects.all(), widget=forms.CheckboxSelectMultiple())

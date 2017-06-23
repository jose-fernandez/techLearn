# -*- encoding: utf-8 -*-

import floppyforms as forms


class DatePicker(forms.DateInput):
    template_name = 'utils/datepicker.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }


class UsuarioForm(forms.Form):
    error_css_class = 'alert alert-danger'

    email = forms.EmailField()
    nombre = forms.CharField(max_length=25)
    apellidos = forms.CharField(max_length=35)
    administrador = forms.BooleanField(required=False)


class CambiarContrasenaForm(forms.Form):
    antigua = forms.CharField(widget=forms.PasswordInput, label='Contraseña Antigua')
    nueva = forms.CharField(widget=forms.PasswordInput, label='Contraseña Nueva')
    renueva = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña Nueva')


class RecuperarContrasenaFormMail(forms.Form):
    nueva = forms.CharField(widget=forms.PasswordInput, label='Contraseña Nueva')
    renueva = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña Nueva')


class RecuperarContrasenaForm(forms.Form):
    email = forms.EmailField()


class ContrasenaForm(forms.Form):
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

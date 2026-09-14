from django import forms

from .models import Alumno, Curso


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'email', 'curso', 'fecha_nacimiento', 'activo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'turno']

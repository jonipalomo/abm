from django.contrib import admin

from .models import Alumno, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'turno')
    search_fields = ('nombre', 'turno')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'curso', 'activo')
    list_filter = ('curso', 'activo')
    search_fields = ('nombre', 'apellido', 'dni')

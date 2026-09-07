from django.contrib import admin

from .models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'curso', 'activo')
    list_filter = ('curso', 'activo')
    search_fields = ('nombre', 'apellido', 'dni')

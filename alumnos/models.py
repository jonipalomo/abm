```python
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.turno}'


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name='alumnos'
    )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

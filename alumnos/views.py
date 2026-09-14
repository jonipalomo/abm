from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AlumnoForm, CursoForm
from .models import Alumno, Curso


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/alumno_list.html'
    context_object_name = 'alumnos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q) | queryset.filter(apellido__icontains=q)
        return queryset


class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnos/alumno_form.html'
    success_url = reverse_lazy('alumnos:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno creado correctamente.')
        return super().form_valid(form)


class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnos/alumno_form.html'
    success_url = reverse_lazy('alumnos:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno actualizado correctamente.')
        return super().form_valid(form)


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumnos/alumno_confirm_delete.html'
    success_url = reverse_lazy('alumnos:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Alumno eliminado correctamente.')
        return super().form_valid(form)


class CursoListView(ListView):
    model = Curso
    template_name = 'alumnos/curso_list.html'
    context_object_name = 'cursos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset


class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'alumnos/curso_form.html'
    success_url = reverse_lazy('alumnos:cursos_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Curso creado correctamente.')
        return super().form_valid(form)


class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'alumnos/curso_form.html'
    success_url = reverse_lazy('alumnos:cursos_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Curso actualizado correctamente.')
        return super().form_valid(form)


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'alumnos/curso_confirm_delete.html'
    success_url = reverse_lazy('alumnos:cursos_lista')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                'No se puede eliminar el curso porque tiene alumnos asignados.'
            )
            return redirect('alumnos:cursos_lista')
        messages.success(self.request, 'Curso eliminado correctamente.')
        return response

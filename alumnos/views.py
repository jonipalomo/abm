from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AlumnoForm
from .models import Alumno


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

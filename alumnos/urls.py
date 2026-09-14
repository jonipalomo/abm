from django.urls import path

from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.AlumnoListView.as_view(), name='lista'),
    path('nuevo/', views.AlumnoCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', views.AlumnoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.AlumnoDeleteView.as_view(), name='eliminar'),
    path('cursos/', views.CursoListView.as_view(), name='cursos_lista'),
    path('cursos/nuevo/', views.CursoCreateView.as_view(), name='cursos_crear'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='cursos_editar'),
    path('cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='cursos_eliminar'),
]

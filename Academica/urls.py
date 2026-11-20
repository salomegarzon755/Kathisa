from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:course_id>/grupos/',views.grupos,name='grupos'),
]

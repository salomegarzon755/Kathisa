from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.listado_cursos, name='lista_cursos'),
    path('cursos/<int:course_id>/grupos/',views.grupos,name='grupos'),
    path('categorias/', views.listado_categoria_curso, name='lista_categoria_cursos'),
    path('categorias/<int:id>/', views.detalle_categoria_curso, name='detalle_categoria_cursos'),
    path('categorias/registrar/',views.registrar_categoria_curso,name='registrar_categoria_curso'),
    path('categorias/actualizar/<int:id>/',views.actualizar_categoria_curso,name='actualizar_categoria_curso',),
    path('categorias/eliminar/<int:id>/',views.eliminar_categoria_curso,name='eliminar_categoria_curso'),
    path('cursos/registrar/', views.registrar_curso, name='registrar_curso'),
    path('cursos/<int:id>/',views.detalle_curso,name='detalle_curso'
),
]

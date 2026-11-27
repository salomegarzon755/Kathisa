from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #urls usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/registrar/', views.registrar_usuarios, name='registrar_usuarios'),
    #urls estudiantes
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/registrar/', views.registrar_estudiante, name='registrar_estudiante'),
    path('estudiantes/<int:student_id>/detalle/', views.detalle_estudiante, name='detalle_estudiante'),
    #urls profesores
    path('profesores/',views.profesores,name='profesores'),
    path('profesores/registrar/',views.registrar_profesor,name='registrar_profesor'),
    path('profesores/<int:teacher_id>/detalle/',views.detalle_profesor,name='detalle_profesor'),
    #urls cursos y grupos
    path('cursos/<int:course_id>/grupos/', views.grupos, name='grupos'),
    path('cursos/<int:course_id>/grupos/registrar/', views.registrar_grupo, name='registrar_grupo'),
    #urls categorias
    path('categorias/', views.listado_categoria_curso, name='lista_categorias'),
    path('cursos/', views.listado_cursos, name='lista_cursos'),
    path('cursos/<int:course_id>/grupos/',views.grupos,name='grupos'),
    path('categorias/<int:id>/', views.detalle_categoria_curso, name='detalle_categoria_cursos'),
    path('categorias/registrar/',views.registrar_categoria_curso,name='registrar_categoria_curso'),
    path('categorias/actualizar/<int:id>/',views.actualizar_categoria_curso,name='actualizar_categoria_curso',),
    path('categorias/eliminar/<int:id>/',views.eliminar_categoria_curso,name='eliminar_categoria_curso'),
    #urls cursos
    path('cursos/registrar/', views.registrar_curso, name='registrar_curso'),
    path('cursos/<int:id>/',views.detalle_curso,name='detalle_curso'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Academica import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', views.usuarios, name='usuarios'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    path('categorias/', views.listado_categorias, name='lista_categorias'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
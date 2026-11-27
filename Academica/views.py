from django.shortcuts import render
from Academica.models import user, student, teacher, course,course_group,course_category
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound


# Create your views here.

def usuarios(request):
    usuarios = user.objects.all().order_by('user_id')
    contexto = {
        'usuarios': usuarios,
        'usuarios_activos': user.objects.filter(is_active=True).count(),
        'usuarios_inactivos': user.objects.filter(is_active=False).count(),
    }
    return render(request, 'usuarios.html', contexto)

def estudiantes(request):
    estudiantes = student.objects.select_related(
        'user',
        'student_status'
    ).all().order_by('student_id')
    contexto = {
        'estudiantes': estudiantes,
        'total_estudiantes': estudiantes.count(),
    }
    return render(request, 'estudiantes.html', contexto)

def profesores(request):
    profesores = teacher.objects.select_related(
        'user',
        'teacher_status'
    ).all().order_by('teacher_id')
    contexto = {
        'profesores': profesores,
        'total_profesores': profesores.count(),
    }
    return render(request, 'profesores.html', contexto)

def cursos(request):
    cursos = course.objects.select_related(
        'course_category',
        'course_status'
    ).all().order_by('course_id')
    contexto = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'cursos.html', contexto)

def grupos(request, course_id):
    curso = get_object_or_404(
        course,
        course_id=course_id
    )
    grupos = course_group.objects.select_related(
        'course',
        'teacher',
        'teacher__user',
        'course_group_status'
    ).filter(
        course_id=course_id
    ).order_by('course_group_id')
    contexto = {
        'curso': curso,
        'grupos': grupos,
        'total_grupos': grupos.count(),
    }
    return render(request, 'grupos.html', contexto)

    
    # LISTADO DE LAS CATEGORIAS

def listado_categorias(request):
    categorias = course_category.objects.all()

    return render(
        request,
        'categorias/listado_categorias.html',
        {'categorias': categorias}
    )


def detalle_categoria(request, id):
    categoria = get_object_or_404(
        course_category,
        course_category_id=id
    )

    return render(
        request,
        'categorias/detalle_categoria.html',
        {'categoria': categoria}
    )

   
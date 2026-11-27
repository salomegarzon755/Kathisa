from Academica.models import user, student, teacher, course,course_group,course_category
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .forms import GruposForm, ProfesoresForm, EstudiantesForm, UsuariosForm


# Create your views here.

def usuarios(request):
    usuarios = user.objects.all().order_by('user_id')
    contexto = {
        'usuarios': usuarios,
        'usuarios_activos': user.objects.filter(is_active=True).count(),
        'usuarios_inactivos': user.objects.filter(is_active=False).count(),
    }
    return render(request, 'usuarios/usuarios.html', contexto)

def registrar_usuarios(request):
    if request.method == 'POST':
        formulario = UsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios')
    else:
        formulario = UsuariosForm()
    return render(request,'usuarios/registrar_usuarios.html',{'formulario': formulario})

#estudiantes

def estudiantes(request):
    estudiantes = student.objects.select_related(
        'user',
        'student_status'
    ).all().order_by('student_id')
    contexto = {
        'estudiantes': estudiantes,
        'total_estudiantes': estudiantes.count(),
    }
    return render(request, 'estudiantes/estudiantes.html', contexto)

def registrar_estudiante(request):
    if request.method == 'POST':
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('estudiantes')
    else:
        formulario = EstudiantesForm()
    return render(request,'estudiantes/registrar_estudiantes.html',
        {'formulario': formulario}
    )

def detalle_estudiante(request, student_id):
    estudiante = get_object_or_404(
        student.objects.select_related(
            'user',
            'student_status'
        ),
        student_id=student_id
    )
    return render(request, 'estudiantes/detalle_estudiante.html',
                {'estudiante': estudiante})

#profesores

def profesores(request):
    profesores = teacher.objects.select_related(
        'user',
        'teacher_status'
    ).all().order_by('teacher_id')
    contexto = {
        'profesores': profesores,
        'total_profesores': profesores.count(),
    }
    return render(request, 'profesores/profesores.html', contexto)

def detalle_profesor(request, teacher_id):
    profesor = get_object_or_404(
        teacher.objects.select_related(
            'user',
            'teacher_status'
        ),
        teacher_id=teacher_id
    )
    return render(request,'profesores/detalle_profesores.html',
        {'profesor': profesor}
    )

def registrar_profesor(request):
    if request.method == 'POST':
        formulario = ProfesoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('profesores')
    else:
        formulario = ProfesoresForm()
    return render(request, 'profesores/registrar_profesores.html',
        {'formulario': formulario}
    )

#cursos

def cursos(request):
    cursos = course.objects.select_related(
        'course_category',
        'course_status'
    ).all().order_by('course_id')
    contexto = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'cursos/cursos.html', contexto)

def detalle_cursos(request):
    cursos = course.objects.select_related(
        'course_category',
        'course_status'
    ).all().order_by('course_id')
    contexto = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'cursos/cursos.html', contexto)

#grupos

def registrar_grupo(request, course_id):
    curso = get_object_or_404(
        course,
        course_id=course_id
    )
    if request.method == 'POST':
        formulario = GruposForm(request.POST, request.FILES)
        if formulario.is_valid():
            grupo = formulario.save(commit=False)
            grupo.course = curso
            grupo.save()
            return redirect('grupos', course_id=curso.course_id)
    else:
        formulario = GruposForm()
    return render(request,'grupos/registrar_grupos.html',
        {'formulario': formulario,'curso': curso}
    )


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
    ).filter(course_id=course_id).order_by('course_group_id')
    contexto = {
        'curso': curso,
        'grupos': grupos,
        'total_grupos': grupos.count(),
    }
    return render(request, 'grupos/grupos.html', contexto)

    
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


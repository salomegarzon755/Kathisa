from django import forms
from Academica.models import course_group, teacher, student, user

class GruposForm(forms.ModelForm):
    class Meta:
        model = course_group
        fields = [
            'course_group_id',
            'teacher',
            'course_group_status',
            'name',
            'start_date',
            'end_date',
            'max_students'
        ]

        widgets = {
            'course_group_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'teacher': forms.Select(attrs={
                'class': 'form-select'
            }),

            'course_group_status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'max_students': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = [
            'teacher_id',
            'user',
            'teacher_status',
            'biography',
            'hire_date',
        ]

        widgets = {
            'teacher_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'user': forms.Select(attrs={
                'class': 'form-select'
            }),

            'teacher_status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe la biografía del profesor'
            }),

            'hire_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = student
        fields = [
            'student_id',
            'user',
            'student_status'
        ]

        widgets = {
            'student_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'user': forms.Select(attrs={
                'class': 'form-select'
            }),

            'student_status': forms.Select(attrs={
                'class': 'form-select'
            }),

        }


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = user
        fields = [
            'user_id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active'
        ]

        widgets = {
            'user_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'is_active': forms.Select(
                choices=[(True, 'Activo'),(False, 'Inactivo')],
                attrs={'class': 'form-select'}
            ),

        }
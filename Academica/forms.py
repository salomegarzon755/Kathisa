from django import forms
from Academica.models import course_category, course


class Category_courseForm(forms.ModelForm):

    class Meta:
        model = course_category
        fields = [
            'course_category_id',
            'category_name',
            'description'
        ]


class Category_courseEditForm(forms.ModelForm):

    class Meta:
        model = course_category
        fields = [
            'category_name',
            'description'
        ]


        
class CourseForm(forms.ModelForm):

    duration_hours = forms.IntegerField(
        min_value=1,
        error_messages={
            'min_value': 'La duración debe ser mayor que cero.'
        }
    )

    min_passing_grade = forms.DecimalField(
        min_value=0,
        error_messages={
            'min_value': 'La nota mínima no puede ser negativa.'
        }
    )

    min_attendance_percentage = forms.DecimalField(
        min_value=0,
        max_value=100,
        error_messages={
            'min_value': 'El porcentaje no puede ser negativo.',
            'max_value': 'El porcentaje no puede superar el 100%.'
        }
    )

    class Meta:
        model = course
        fields = [
            'course_id',
            'course_category',
            'course_status',
            'name',
            'description',
            'duration_hours',
            'min_passing_grade',
            'min_attendance_percentage'
        ]
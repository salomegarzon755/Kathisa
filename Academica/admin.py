from django.contrib import admin
from .models import user_status, gender, user, user_profile, admin_status, administrator, student_status, student, teacher_status, teacher, course_status, course_category, course, course_group_status, course_group, enrollment_status, enrollment, modality, session_status, class_session, schedule, attendance_status, attendance, evaluation, assignment_submission, grade, certificate, notification

# Register your models here.


admin.site.register(user_status)
admin.site.register(gender)
admin.site.register(user)
admin.site.register(user_profile)
admin.site.register(admin_status)
admin.site.register(administrator)
admin.site.register(student_status)
admin.site.register(student)
admin.site.register(teacher_status)
admin.site.register(teacher)
admin.site.register(course_status)
admin.site.register(course_category)
admin.site.register(course)
admin.site.register(course_group_status)
admin.site.register(course_group)
admin.site.register(enrollment_status)
admin.site.register(enrollment)
admin.site.register(modality)
admin.site.register(session_status)
admin.site.register(class_session)
admin.site.register(schedule)
admin.site.register(attendance_status)
admin.site.register(attendance)
admin.site.register(evaluation)
admin.site.register(assignment_submission)
admin.site.register(grade)
admin.site.register(certificate)
admin.site.register(notification) 

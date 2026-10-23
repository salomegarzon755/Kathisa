from django.db import models

# Create your models here.
## CLASES SIN FOREIGN KEY

from django.db import models

class user_status(models.Model):
    user_status_id = models.PositiveBigIntegerField(primary_key=True)
    name_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_status'

class gender(models.Model):
    gender_id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'gender'

class user(models.Model):
    user_id = models.PositiveBigIntegerField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'user'

class user_profile(models.Model):
    user_profile_id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    user_status = models.ForeignKey(user_status, on_delete=models.RESTRICT, db_column='user_status_id')
    document_type = models.CharField(max_length=30)
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    gender = models.ForeignKey(gender, on_delete=models.RESTRICT, db_column='gender_id')

    class Meta:
        db_table = 'user_profile'

class admin_status(models.Model):
    admin_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin_status'

class admin(models.Model):
    admin_id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    admin_status = models.ForeignKey(admin_status, on_delete=models.RESTRICT, db_column='admin_status_id')
    hire_date = models.DateField()

    class Meta:
        db_table = 'admin'

class student_status(models.Model):
    student_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'student_status'

class student(models.Model):
    student_id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    student_status = models.ForeignKey(student_status, on_delete=models.RESTRICT, db_column='student_status_id')

    class Meta:
        db_table = 'student'

class teacher_status(models.Model):
    teacher_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teacher_status'

class teacher(models.Model):
    teacher_id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    teacher_status = models.ForeignKey(teacher_status, on_delete=models.RESTRICT, db_column='teacher_status_id')
    biography = models.TextField()
    hire_date = models.DateField()

    class Meta:
        db_table = 'teacher'

class course_status(models.Model):
    course_status_id = models.PositiveBigIntegerField(primary_key=True)
    course_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'course_status'

class course_category(models.Model):
    course_category_id = models.PositiveBigIntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'course_category'

class course(models.Model):
    course_id = models.PositiveBigIntegerField(primary_key=True)
    course_category = models.ForeignKey(course_category, on_delete=models.RESTRICT, db_column='course_category_id')
    course_status = models.ForeignKey(course_status, on_delete=models.RESTRICT, db_column='course_status_id')
    name = models.CharField(max_length=150)
    description = models.TextField()
    duration_hours = models.IntegerField()
    min_passing_grade = models.DecimalField(max_digits=3, decimal_places=2)
    min_attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'course'

class course_group_status(models.Model):
    course_group_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'course_group_status'

class course_group(models.Model):
    course_group_id = models.PositiveBigIntegerField(primary_key=True)
    course = models.ForeignKey(course, on_delete=models.CASCADE, db_column='course_id')
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True, db_column='teacher_id')
    course_group_status = models.ForeignKey(course_group_status, on_delete=models.RESTRICT, db_column='course_group_status_id')
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.IntegerField()

    class Meta:
        db_table = 'course_group'

class enrollment_status(models.Model):
    enrollment_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'enrollment_status'

class enrollment(models.Model):
    enrollment_id = models.PositiveBigIntegerField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, db_column='student_id')
    course_group = models.ForeignKey(course_group, on_delete=models.CASCADE, db_column='course_group_id')
    enrollment_status = models.ForeignKey(enrollment_status, on_delete=models.RESTRICT, db_column='enrollment_status_id')
    enrollment_date = models.DateField()

    class Meta:
        db_table = 'enrollment'

class modality(models.Model):
    modality_id = models.PositiveBigIntegerField(primary_key=True)
    modality_name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'modality'

class session_status(models.Model):
    session_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'session_status'

class class_session(models.Model):
    class_session_id = models.PositiveBigIntegerField(primary_key=True)
    course_group = models.ForeignKey(course_group, on_delete=models.CASCADE, db_column='course_group_id')
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True, db_column='teacher_id')
    modality = models.ForeignKey(modality, on_delete=models.RESTRICT, db_column='modality_id')
    session_status = models.ForeignKey(session_status, on_delete=models.RESTRICT, db_column='session_status_id')
    title = models.CharField(max_length=150)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meet_link = models.CharField(max_length=200)
    classroom_location = models.CharField(max_length=100)

    class Meta:
        db_table = 'class_session'

class schedule(models.Model):
    schedule_id = models.PositiveBigIntegerField(primary_key=True)
    course_group = models.ForeignKey(course_group, on_delete=models.CASCADE, db_column='course_group_id')
    modality = models.ForeignKey(modality, on_delete=models.RESTRICT, db_column='modality_id')
    day_week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'schedule'

class attendance_status(models.Model):
    attendance_status_id = models.PositiveBigIntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'attendance_status'

class attendance(models.Model):
    attendance_id = models.PositiveBigIntegerField(primary_key=True)
    class_session = models.ForeignKey(class_session, on_delete=models.CASCADE, db_column='class_session_id')
    enrollment = models.ForeignKey(enrollment, on_delete=models.CASCADE, db_column='enrollment_id')
    attendance_status = models.ForeignKey(attendance_status, on_delete=models.RESTRICT, db_column='attendance_status_id')
    modality = models.ForeignKey(modality, on_delete=models.RESTRICT, db_column='modality_id')
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True, db_column='teacher_id')
    attendance_source = models.CharField(max_length=10)
    arrive_time = models.TimeField()
    departure_time = models.TimeField()
    observations = models.TextField()

    class Meta:
        db_table = 'attendance'

class evaluation(models.Model):
    evaluation_id = models.PositiveBigIntegerField(primary_key=True)
    course_group = models.ForeignKey(course_group, on_delete=models.CASCADE, db_column='course_group_id')
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True, db_column='teacher_id')
    evaluation_name = models.CharField(max_length=150)
    evaluation_type = models.CharField(max_length=20)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    evaluation_date = models.DateField()
    due_date = models.DateField()
    allow_late_evaluation = models.BooleanField()

    class Meta:
        db_table = 'evaluation'

class assigment_submission(models.Model):
    submission_id = models.PositiveBigIntegerField(primary_key=True)
    evaluation = models.ForeignKey(evaluation, on_delete=models.CASCADE, db_column='evaluation_id')
    enrollment = models.ForeignKey(enrollment, on_delete=models.CASCADE, db_column='enrollment_id')
    submission_date = models.DateTimeField()
    submission_uri = models.CharField(max_length=200)
    submission_text = models.TextField()
    submission_status = models.CharField(max_length=15)

    class Meta:
        db_table = 'assigment_submission'

class grade(models.Model):
    grade_id = models.PositiveBigIntegerField(primary_key=True)
    evaluation = models.ForeignKey(evaluation, on_delete=models.CASCADE, db_column='evaluation_id')
    enrollment = models.ForeignKey(enrollment, on_delete=models.CASCADE, db_column='enrollment_id')
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True, db_column='teacher_id')
    gredue_value = models.DecimalField(max_digits=3, decimal_places=2)
    feedback = models.TextField()
    graded_at = models.DateTimeField()

    class Meta:
        db_table = 'grade'

class certificate(models.Model):
    certificate_id = models.PositiveBigIntegerField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, db_column='student_id')
    admin = models.ForeignKey(admin, on_delete=models.SET_NULL, null=True, blank=True, db_column='admin_id')
    certicate_code = models.CharField(max_length=30)
    issue_date = models.DateField()

    class Meta:
        db_table = 'certificate'

class notificacion(models.Model):
    notificacion_id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    title = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField()
    is_read = models.BooleanField()
    read_at = models.DateTimeField()

    class Meta:
        db_table = 'notificacion'
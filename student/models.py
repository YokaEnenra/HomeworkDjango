from django.db.models import Model, CharField, PositiveIntegerField, DateTimeField, BooleanField, \
    OneToOneField, ForeignKey, ManyToManyField, RESTRICT


class Person(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    social_url = CharField(max_length=100, blank=True)
    email = CharField(max_length=100, blank=True)
    age = PositiveIntegerField()
    STUDENT = 'STD'
    TEACHER = 'TCH'
    PERSON_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    person_type = CharField(max_length=3, choices=PERSON_TYPE_CHOICES, default=STUDENT)
    # Many persons to one group
    student_group = ForeignKey('Group', on_delete=RESTRICT, null=True)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)
    active_acc = BooleanField(default=True)


class Group(Model):
    name = CharField(max_length=4, default=None)
    headman = OneToOneField('Person', on_delete=RESTRICT, null=True)
    edu_program = CharField(max_length=100)
    # Many groups to one course
    course = ForeignKey('Course', on_delete=RESTRICT, null=True)
    subjects = ManyToManyField('Subject', null=True)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Subject(Model):
    name = CharField(max_length=30, default=None)
    courses = ManyToManyField('Course', null=True)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Course(Model):
    name = CharField(max_length=50, default=None)
    curator = OneToOneField('Person', on_delete=RESTRICT, null=True)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Lesson(Model):
    # Many lessons to one subject
    subject = ForeignKey('Subject', on_delete=RESTRICT, null=True)
    teacher = OneToOneField('Person', on_delete=RESTRICT, null=True)
    theme = CharField(max_length=100)
    groups = ManyToManyField('Group', null=True)
    date_of_lesson = DateTimeField(null=True)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)

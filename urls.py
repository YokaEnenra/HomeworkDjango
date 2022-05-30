"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from student.views import home_page, bonus_page, welcome_page, get_email_verification, \
    get_reset_password, Students, NewPerson, NewSubject, StudentDetail, PersonUpdate, Teachers, SubjectDetail, \
    SubjectUpdate, Subjects, SendEmail, signin, signout, signup, verify_account

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', general_page),
    path('', home_page, name='home'),
    path('home/easter', bonus_page),
    path('reg', welcome_page),
    path('verify_email', get_email_verification),
    path('reset_pass', get_reset_password),
    path('home/easter', bonus_page),
    path('students', Students.as_view(), name='students_list'),
    path('teachers', Teachers.as_view(), name='teachers_list'),
    path('person/create', NewPerson.as_view(), name='create_person'),
    path('person/detail/<int:pk>', StudentDetail.as_view(), name='person_detail'),
    path('person/update/<int:pk>', PersonUpdate.as_view(), name='person_update'),
    path('subjects', Subjects.as_view(), name='subjects_list'),
    path('subject/create', NewSubject.as_view(), name='create_subject'),
    path('subject/detail/<int:pk>', SubjectDetail.as_view(), name='subject_details'),
    path('subject/update/<int:pk>', SubjectUpdate.as_view(), name='subject_update'),
    path('send_mail', SendEmail.as_view()),
    path('login', signin, name='login'),
    path('logout', signout, name='logout'),
    path('register/<str:error_message>', signup, name='register_with_error'),
    path('register', signup, name='register'),
    path('verify/<str:uid>/<str:token>', verify_account, name='verify_account')
]

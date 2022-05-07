from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from student.email import send
from student.forms import MessageForm
from student.models import Person, Subject


def home_page(request):
    return HttpResponse('Maybe you are searching for "/students","/teachers","/subjects"')


def general_page(request):
    return HttpResponse('This is not the page you are looking for(try "/home" page)')


def bonus_page(request):
    return HttpResponse("Hey, what are you looking here")


def get_email_verification(request):
    return render(request, "email_verification.html")


def get_reset_password(request):
    return render(request, "reset_password.html")


def welcome_page(request):
    return render(request, "welcome_email.html")


class Students(View):
    def get(self, request):
        persons = Person.objects.all().filter(person_type='STD')
        return render(request, "persons_list.html", context={
            "persons": persons,
        })


class StudentDetail(DetailView):
    model = Person
    template_name = "person_detail.html"


class NewPerson(CreateView):
    model = Person
    template_name = "new_person.html"
    fields = ['first_name', 'last_name', 'age', 'person_type']
    success_url = reverse_lazy('students_list')


class PersonUpdate(UpdateView):
    model = Person
    template_name = "person_edit.html"
    fields = ['first_name', 'last_name', 'age', 'person_type', 'active_acc']
    success_url = reverse_lazy('home')


class Teachers(View):
    def get(self, request):
        persons = Person.objects.all().filter(person_type='TCH')
        return render(request, "persons_list.html", context={
            "persons": persons,
        })


class Subjects(ListView):
    model = Subject
    template_name = "subjects_list.html"


class NewSubject(CreateView):
    model = Subject
    template_name = "new_subject.html"
    fields = ['teacher', 'name']
    success_url = reverse_lazy('students_list')


class SubjectDetail(DetailView):
    model = Subject
    template_name = "subject_detail.html"


class SubjectUpdate(UpdateView):
    model = Subject
    template_name = "subject_edit.html"
    fields = ['name', 'teacher']
    success_url = reverse_lazy('home')


class SendEmail(View):
    def get(self, request):
        return render(request, "choose_email.html", context={'form': MessageForm})

    def post(self, request):

        send(
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
            to_email=request.POST.get("to_email"),
            template_name='send_email.html',
            context={
                'subject': request.POST.get("subject"),
                'message': request.POST.get("message")
            }
        )
        return redirect(reverse_lazy('home'))

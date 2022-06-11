from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from rest_framework import viewsets, permissions

from student.email import send
from student.forms import MessageForm
from student.models import Person, Subject, Group
from student.serializers import PersonSerializer, GroupSerializer, SubjectSerializer, PersonRetrieveSerializer, \
    GroupRetrieveSerializer, SubjectRetrieveSerializer

USER_MODEL = get_user_model()


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
        if request.user.is_authenticated:
            persons = Person.objects.all().filter(person_type='STD')
            return render(request, "persons_list.html", context={
                "persons": persons,
            })
        else:
            return HttpResponse("You are not logged in")


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


def signin(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f"Hello, {user.username}!")
        else:
            return HttpResponse("Invalid username or password, pls check your input or contact our TechSupport")


def signout(request):
    logout(request)
    return redirect(reverse_lazy('login'))


def signup(request, error_message=None):
    if request.method == "GET":
        return render(request, "register.html", context={'error_message': error_message})
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if USER_MODEL.objects.filter(username=username).exists():
            return redirect(reverse_lazy('register_with_error', kwargs={
                'error_message': 'Username already exists'}))
        if USER_MODEL.objects.filter(email=email).exists():
            return redirect(reverse_lazy('register_with_error', kwargs={
                'error_message': 'User with that email already exists'}))
        user = USER_MODEL.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False)
        send(subject='Verification Email',
             to_email=user.email,
             template_name='verification_email.html',
             context={'subject': f'Hi, {user.username}.',
                      'link': reverse_lazy('verify_account', kwargs={
                          'uid': urlsafe_base64_encode(force_bytes(user.id)),
                          'token': default_token_generator.make_token(user)}),
                      'request': request})
        return HttpResponse(f"Hello, {user.username}. Your account successfully "
                            "created, now you need to activate it, "
                            "via activation letter, that is send to your email")


def verify_account(request, uid, token):
    try:
        user = USER_MODEL.objects.get(id=urlsafe_base64_decode(uid))
    except (TypeError, ValueError, OverflowError, USER_MODEL.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse(f"Hello, {user.username}!")
    return HttpResponse('Invalid token, try again or contact our TechSupport')


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PersonRetrieveSerializer
        return PersonSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GroupRetrieveSerializer
        return GroupSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SubjectRetrieveSerializer
        return SubjectSerializer

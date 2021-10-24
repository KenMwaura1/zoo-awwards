from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from z_awwards.forms import ProjectForm, RegisterForm
from z_awwards.models import UserProject


def home(request):
    """
    Home page
    :param request:
    :return: home template
    """
    random_project = None
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
        else:
            form = ProjectForm()
        try:
            all_projects = UserProject.all_posts()
            random_project = UserProject.random_post()
        except UserProject.DoesNotExist:
            all_projects = None

        return render(request, 'z_awwards/home.html', {'all_projects': all_projects, 'random_project': random_project})


def register(request):
    """
    Register page
    :param request:
    :return:
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'django_registration/registration_form.html', {'form': form})


@login_required(login_url='/login/')
def profile(request, username):
    return render(request, 'z_awwards/profile.html')


def user_profile(request):
    return None


def search_profile(request):
    return None

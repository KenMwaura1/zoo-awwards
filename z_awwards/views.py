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




def user_profile(request):
    return None


def search_profile(request):
    return None

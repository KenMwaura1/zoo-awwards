from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from z_awwards.forms import ProjectForm, RegisterForm, UpdateUserForm, UpdateUserProfileForm, ProjectRatingForm
from z_awwards.models import UserProject, ProjectRating


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


def user_profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    if request.user == user_profile:
        return redirect('profile', username=request.user.username)
    params = {'user_profile': user_profile}
    return render(request, 'z_awwards/user_profile.html', params)


@login_required(login_url='/login/')
def user_projects(request, username):
    """
    User projects page
    :param request:
    :param username:
    :return: user_projects page
    """
    user_profile = get_object_or_404(User, username=username)
    if request.user == user_profile:
        return redirect('profile', username=request.user.username)
    params = {'user_profile': user_profile}
    return render(request, 'z_awwards/user_projects.html', params)


@login_required(login_url='/login/')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        profile_form = UpdateUserProfileForm(request.POST, instance=request.user.userprofile)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile', user.username)
    else:
        profile_form = UpdateUserProfileForm(request.POST, instance=request.user.userprofile)
        user_form = UpdateUserForm(request.POST, instance=request.user)
    params = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'z_awwards/edit_profile.html', params)


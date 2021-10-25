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


@login_required(login_url='/login/')
def single_project(request, project):
    """
    get single_project
    :param request:
    :return:
    """
    project = UserProject.objects.get(title=project)
    project_ratings = ProjectRating.objects.filter(user=request.user, project=project).first()
    rating_status = project_ratings is not None
    if request.method == "POST":
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.project = project
            rating.save()
            project_ratings = ProjectRating.objects.filter(project=project).first()
            design_score = [d.design for d in project_ratings]
            design_average = sum(design_score) / len(design_score)
            usability_score = [u.usability for u in project_ratings]
            usability_average = sum(usability_score) / len(usability_score)
            content_score = [c.content for c in project_ratings]
            content_average = sum(content_score) / len(content_score)

            total_score = (design_average + usability_average + content_average) / 3
            print(total_score)
            rating.design_average = round(design_average, 2)
            rating.usability_average = round(usability_average, 2)
            rating.content_average = round(content_average, 2)
            rating.total_score = round(total_score, 2)
            rating.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProjectRatingForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
    }
    return render(request, 'z_awwards/single_project.html', params)


def search_projects(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            projects = UserProject.objects.filter(title__icontains=query)
            message = f'{len(projects)} results found for {query}'
            params = {
                'projects': projects,
                'query': query,
                'message': message,
            }
            return render(request, 'z_awwards/search_projects.html', params)
        else:
            message = 'Please enter a search term'
        return render(request, 'z_awwards/search_projects.html', {'message': message})

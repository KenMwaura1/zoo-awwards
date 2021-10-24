from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from z_awwards.models import UserProject, ProjectRating


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProjectForm(ModelForm):
    """
    Form for creating a new project.
    """

    class Meta:
        model = UserProject
        fields = ('title', 'description', 'url', 'photo', 'technologies')


class ProjectRatingForm(ModelForm):
    """
    form for creating ratings
    """

    class Meta:
        model = ProjectRating
        fields = ['design', 'usability', 'content']
        labels = {
            'design': 'Design',
            'usability': 'Usability',
            'content': 'Content'
        }

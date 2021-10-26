
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from z_awwards.models import UserProject, ProjectRating, UserProfile


class RegisterForm(UserCreationForm):
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
    # photo = forms.ImageField(required=False, label='Project Photo')

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


class UpdateUserForm(ModelForm):
    """
    Form for updating user information.
    """
    email = forms.EmailField(required=True, label='Email', max_length=150, help_text='Enter valid email address')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(ModelForm):
    """
    Form for updating user profile.
    """
    username = forms.CharField(required=True, label='Name', max_length=150, help_text='Enter valid username')

    class Meta:
        model = UserProfile
        fields = ['username', 'location', 'profile_pic', 'bio', ]




class UpdateRatingForm(ModelForm):
    """
    Form for updating project rating.
    """

    class Meta:
        model = ProjectRating
        fields = ['design', 'usability', 'content']
        labels = {
            'design': 'Design',
            'usability': 'Usability',
            'content': 'Content'
        }

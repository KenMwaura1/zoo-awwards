from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserProject, ProjectRating


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model
    """

    class Meta:
        model = UserProject
        fields = ['id', 'title', 'user', 'project', 'url', 'description', 'date', ]


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model
    """

    class Meta:
        model = UserProfile
        fields = ['username', 'profile_pic', 'bio', 'location', 'date_joined']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    project = ProjectSerializer(many=True, read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'userprofile', 'project', 'profile')

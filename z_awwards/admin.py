from django.contrib import admin

from .models import UserProfile, UserProject, ProjectRating

admin.site.register(UserProfile)
admin.site.register(UserProject)
admin.site.register(ProjectRating)

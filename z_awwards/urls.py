from django.urls import include, path
from rest_framework import routers

from z_awwards import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectViewSet)
router.register('profiles', views.ProfileViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('user_profile/<username>/settings', views.edit_profile, name='edit_profile'),
    path('project/<project>', views.single_project, name='single_project'),
    path('user_profile/<username>/projects', views.user_projects, name='user_projects'),
    path('search/', views.search_projects, name='search'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    ]

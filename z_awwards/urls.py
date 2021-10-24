from django.urls import include, path

from z_awwards import views

urlpatterns = [
    path('', views.home, name='home'),
    ]
from django.urls import include, path
from . import views
from rest_framework import routers



urlpatterns = [
    path('user/signup', views.signup),
    path('user/login', views.login),
    path('user/<int:user_id>', views.get_user),
]


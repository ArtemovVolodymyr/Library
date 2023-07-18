from django.urls import include, path
from . import views
from rest_framework import routers


urlpatterns = [
    path('user/', views.signup_or_login),
    path('user/<int:user_id>', views.get_user),
]


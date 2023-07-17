from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.users_view, name='users'),
    path('users/<int:user_id>/', views.user_view, name='user'),
]

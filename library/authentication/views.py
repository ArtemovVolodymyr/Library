from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from authentication.selectors.user import all_users, get_user_by_id_or_none
from authentication.services.user import user_create
from utils.errors import message_to_html_alert, messages_to_html_alert


def login_view(request):
    context = {}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if user := authenticate(request, email=email, password=password):
            login(request, user)
            return redirect('/')
        else:
            context['alerts'] = message_to_html_alert('Incorrect login or password', 'danger')

    return render(request, 'authentication/login.html', context)


@csrf_exempt
def registration_view(request):
    context = {}

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        role = int(request.POST['role'])

        if password != password_confirmation:
            context['alerts'] = message_to_html_alert('Passwords do not match', 'danger')
        else:
            try:
                user_create(
                    email=email,
                    password=password,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    role=role
                )
            except ValidationError as errors:
                context['alerts'] = messages_to_html_alert(errors, 'danger')
            else:
                context['alerts'] = message_to_html_alert('You have successfully registered!', 'success')

    return render(request, 'authentication/registration.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')


def users_view(request):
    if request.method == 'GET':
        context = {'users': all_users()}
        return render(request, 'authentication/users.html', context)


def user_view(request, user_id):
    if request.method == 'GET':
        context = {'specific_user': get_user_by_id_or_none(user_id)}
        return render(request, 'authentication/user.html', context)

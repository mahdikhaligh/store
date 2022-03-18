from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import LoginForm, RegisterForm, EditUserAccountForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = LoginForm(request.POST or None)

    if form_login.is_valid():
        username = form_login.cleaned_data.get('username')
        password = form_login.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form_login.add_error('username', 'this username is not valid or not register')
    context = {
        'title': 'Login',
        'form_login': form_login
    }

    return render(request, 'account/Login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form_register = RegisterForm(request.POST or None)

    if form_register.is_valid():
        username = form_register.cleaned_data.get('username')
        password = form_register.cleaned_data.get('password')
        email = form_register.cleaned_data.get('email')

        User.objects.create_user(username=username, password=password, email=email)
        return redirect('/login')

    context = {
        'title': 'Register',
        'form_register': form_register
    }

    return render(request, 'account/Register.html', context)


def log_out_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()

    context = {
        'title': 'panel-user',
        'user': user
    }

    return render(request, 'account/user_account_main.html', context)


@login_required(login_url='/login')
def user_edit_account(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('this not found user')
    edit_user_form = EditUserAccountForm(
        request.POST or None,
        initial={
                'first_name': user.first_name,
                'last_name': user.last_name
        })
    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        'title': 'edit-account',
        'edit_user': edit_user_form
    }

    return render(request, 'account/user_edit_account.html', context)


@login_required(login_url='/login')
def user_sidebar(request):
    return render(request, 'account/user_sidebar_panel.html', {})

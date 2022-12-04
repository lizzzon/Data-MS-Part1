from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from apps.authentication.handlers import AuthenticationHandler
from apps.authentication.forms import LoginForm, RegisterForm


class LoginView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name='authentication/login.html', context={'form': LoginForm})

    def post(self, request: HttpRequest) -> HttpResponse:
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            if AuthenticationHandler.login_handler(request=request, login_form=login_form):
                return redirect(to='base')

        return render(request=request, template_name='authentication/login.html', context={'form': login_form})


class RegisterView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name='authentication/register.html', context={'form': RegisterForm})

    def post(self, request: HttpRequest) -> HttpResponse:
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            AuthenticationHandler.register_handler(request=request, register_form=register_form)
            return redirect(to='login')

        return render(request=request, template_name='authentication/register.html', context={'form': register_form})

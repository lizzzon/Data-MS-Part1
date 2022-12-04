from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required


class ProfileView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request: HttpRequest) -> HttpResponse:
        #profile_form = ProfileForm()
        return render(request=request, template_name='base/profile.html',) #context={'form': profile_form})

    @method_decorator(login_required(login_url='login'))
    def post(self, request: HttpRequest) -> HttpResponse:
        # profile_form = ProfileForm()
        return render(request=request, template_name='base/profile.html',) #context={'form': profile_form})

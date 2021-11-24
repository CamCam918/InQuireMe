from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import (
    TemplateView
)

# Create your views here.
class HomePageView(TemplateView):
    template_name="base.html"

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registrations/signup.html'

class LoginView(generic.CreateView):
    template_name = 'registrations/login.html'
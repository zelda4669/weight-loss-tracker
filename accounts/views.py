from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


class SettingsView(LoginRequiredMixin, ListView):
    template_name = 'settings.html'
    model = CustomUser

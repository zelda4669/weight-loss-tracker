from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Measurements

class HomePageView(ListView):
    template_name = 'home.html'
    model = Measurements
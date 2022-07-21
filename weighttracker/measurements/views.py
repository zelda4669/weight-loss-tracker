from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from .models import Measurements


class HomePageView(ListView):
    template_name = 'home.html'
    model = Measurements


class AddMeasurementView(CreateView):
    template_name = 'add_measurements.html'
    model = Measurements
    fields = ['date', 'weight', 'bust', 'chest', 'waist', 'hips', 'left_thigh', 'right_thigh', 'left_calf',
              'right_calf', 'left_forearm', 'right_forearm', 'left_upper_arm', 'right_upper_arm']
    def get_success_url(self):
        return reverse('home')

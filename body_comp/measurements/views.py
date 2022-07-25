from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Measurement


class HomePageView(ListView):
    template_name = 'home.html'
    model = Measurement


class AddMeasurementView(CreateView):
    template_name = 'add_measurements.html'
    model = Measurement
    fields = ['date', 'weight', 'bust', 'chest', 'waist', 'hips', 'left_thigh', 'right_thigh', 'left_calf',
              'right_calf', 'left_forearm', 'right_forearm', 'left_upper_arm', 'right_upper_arm']
    success_url = reverse_lazy('home')

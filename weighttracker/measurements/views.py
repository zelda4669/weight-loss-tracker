from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Enter your stats here.')

# Create your views here.

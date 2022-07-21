from django.urls import path
from .views import HomePageView, AddMeasurementView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("add_measurement", AddMeasurementView.as_view(), name='add_measurement'),
]

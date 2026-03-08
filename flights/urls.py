from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList.as_view(), name='home'),
]
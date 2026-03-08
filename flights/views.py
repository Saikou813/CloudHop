from django.shortcuts import render
from django.views import generic
from .models import Flight

# Create your views here.

class FlightList(generic.ListView):
    model = Flight
    template_name = 'index.html'
    context_object_name = 'flights'
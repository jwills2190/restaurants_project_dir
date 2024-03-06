from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Restaurant
# Create your views here.

class RestaurantListView(ListView):
    model = Restaurant
    
class RestaurantDetailView(DetailView):
    model = Restaurant
    
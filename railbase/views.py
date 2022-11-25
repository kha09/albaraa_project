from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import File


class HomePageView(ListView):
    model = File
    template_name = "home.html"
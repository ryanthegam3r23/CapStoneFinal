from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stat
# Create your views here.
class StatList(ListView):
    model = Stat
    template_name = "stat/list.html"



class StatDetail(DetailView):
    model = Stat
    template_name = "stat/details.html"
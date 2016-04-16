from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from models import *

# Create your views here.


def mainpage(request):
    return HttpResponse('CARS')

class MarcaList(ListView):
    model = Marca

class ModelList(ListView):
    model = Model

class EstilDetail(DetailView):
    model = Estil
    queryset = Estil.objects.order_by('year')[:10]

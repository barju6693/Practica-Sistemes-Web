from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from models import Marca, Model, Motor, Year, Estil
from forms import *


def mainpage(request):
    return HttpResponse('CARS')


class MarcaList(ListView):
    model = Marca
    context_object_name = 'brand_list'
    template_name = 'icars/brand_list.html'


class MarcaCreate(CreateView):
    model = Marca
    template_name = 'icars/form.html'
    form_class = MarcaForm

class MarcaDetail(DetailView):
    model = Marca
    template_name = 'icars/brand_detail.html'

class MarcaDelete(DeleteView):
    model = Marca
    success_url = reverse_lazy('brand_list')


class ModelList(ListView):
    model = Model

class ModelCreate(CreateView):
    model = Model
    template_name = 'icars/form.html'
    form_class = ModelForm

class ModelDetail(DetailView):
    model = Model
    template_name = 'icars/model_detail.html'

class ModelDelete(DeleteView):
    model = Model
    success_url = reverse_lazy('model_list')

class EstilList(ListView):
    model = Estil
    context_object_name = 'style_list'
    template_name = 'icars/style_list.html'

class EstilCreate(CreateView):
    model = Estil
    template_name = 'icars/form.html'
    form_class = EstilForm

class EstilDetail(DetailView):
    model = Estil
    template_name = 'icars/style_detail.html'

class EstilDelete(DeleteView):
    model = Estil
    success_url = reverse_lazy('style_list')


class MotorList(ListView):
    model = Motor
    template_name = 'icars/motor_list.html'

class MotorCreate(CreateView):
    model = Motor
    template_name = 'icars/form.html'
    form_class = MotorForm

class MotorDetail(DetailView):
    model = Motor
    template_name = 'icars/motor_detail.html'

class MotorDelete(DeleteView):
    model = Motor
    success_url = reverse_lazy('motor_list')

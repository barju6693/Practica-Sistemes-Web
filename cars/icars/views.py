from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from models import *
from forms import *

# Create your views here.


def mainpage(request):
    return HttpResponse('CARS')


class MarcaList(ListView):
    model = Marca
    context_object_name = 'marques_list'
    template_name = 'icars/marca_list.html'

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'icars/form.html'
    form_class = MarcaForm

    #def form_valid(self, form):
    #    form.instance.niceName = self.request.niceName
    #    return super(MarcaCreate, self).form_valid(form)


class MarcaDetail(DetailView):
    model = Marca
    template_name = 'icars/marca_detail.html'


class ModelList(ListView):
    model = Model


class ModelCreate(CreateView):
    model = Model
    template_name = 'icars/form.html'
    form_class = ModelForm

    """def form_valid(self, form):
        form.instance.name = self.request.name
        return super(ModelCreate, self).form_valid(form)"""


class ModelDetail(DetailView):
    model = Model
    template_name = 'icars/model_detail.html'


class EstilList(ListView):
    model = Estil
    context_object_name = 'styles_list'
    template_name = 'icars/style_list.html'


class EstilCreate(CreateView):
    model = Estil
    template_name = 'icars/form.html'
    form_class = EstilForm

    def form_valid(self, form):
        form.instance.name = self.request.name
        return super(EstilCreate, self).form_valid(form)


class EstilDetail(DetailView):
    model = Estil
    template_name = 'icars/style_detail.html'


class MotorList(ListView):
    model = Motor
    template_name = 'icars/motor_list.html'


class MotorCreate(CreateView):
    model = Motor
    template_name = 'icars/form.html'
    form_class = MotorForm

    def form_valid(self, form):
        form.instance.name = self.request.name
        return super(MotorCreate, self).form_valid(form)


class MotorDetail(DetailView):
    model = Motor
    template_name = 'icars/motor_detail.html'

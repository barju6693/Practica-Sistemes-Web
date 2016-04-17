from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from models import *
from forms import MarcaForm, ModelForm

# Create your views here.


def mainpage(request):
    return HttpResponse('CARS')

class MarcaList(ListView):
    model = Marca
    context_object_name = 'marques_list'
    template_name = 'icars/marca_list.html'

#abortem el create per pract2
#class MarcaCreate(CreateView):
#    model = Marca
#    template_name = 'icars/form.html'
#    form_class = MarcaForm
#
#    def form_valid(self, form):
#        form.instance.name = self.request.name
#        return super(MarcaCreate, self).form_valid(form)

class ModelList(ListView):
    model = Model

class ModelDetail(DetailView):
    model = Model
    template_name = 'icars/model_detail.html'

class EstilList(ListView):
    model = Estil
    context_object_name = 'styles_list'
    template_name = 'icars/style_list.html'

class EstilDetail(DetailView):
    model = Estil
    template_name = 'icars/style_detail.html'

class MotorList(ListView):
    model = Motor
    template_name = 'icars/motor_list.html'

class MotorDetail(DetailView):
    model = Motor
    template_name = 'icars/motor_detail.html'

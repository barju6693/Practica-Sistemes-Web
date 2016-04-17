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

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'icars/form.html'
    form_class = MarcaForm

    def form_valid(self, form):
        form.instance.marca = Marca.objects.get(id=self.kwargs['pk'])
        return super(MarcaCreate, self).form_valid(form)

class ModelList(ListView):
    model = Model

class EstilDetail(DetailView):
    model = Estil
    queryset = Estil.objects.order_by('year')[:10]

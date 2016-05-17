from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.views.generic.base import RedirectView

from models import *
from views import *

urlpatterns = [
    #home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('icars:marca_list', kwargs={'extension': 'html'})),
        name='home_page'),

        #url(r'^home\.(?P<extension>(json|xml|html))$',
        #    HomePage.as_view(),
        #    name='home'),
    # List all brands: /icars/marques.json
    url(r'^marques\.(?P<extension>(json|xml|html))$',
        MarcaList.as_view(),
        name='marca_list'),
        # Restaurant details, ex.: /myrestaurants/restaurants/1.json
        url(r'^marques/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
            MarcaDetail.as_view(),
            name='marca_detail'),
    # List all models: /icars/models.json
    url(r'^models\.(?P<extension>(json|xml|html))$',
        ModelList.as_view(),
        name='model_list'),

    url(r'^models/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        ModelDetail.as_view(),
        name='model_detail'),
    #List 10 styles : /icars/estil.json
    url(r'^estil\.(?P<extension>(json|xml|html))$',
        EstilList.as_view(),
        name='style_list'),

    #url(r'^estil/details\.(?P<extension>(json|xml|html))$',
    #    EstilDetail.as_view(),
    #    name='style_detail'),

    #Detail of a style: /icars/estil/1.html
    url(r'^estil/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        EstilDetail.as_view(),
        name='style_detail'),
    #List all motors: /icars/motor.html
    url(r'^motor\.(?P<extension>(json|xml|html))$',
        MotorList.as_view(),
        name='motor_list'),
    #Detail of a motor: icars/motor/1.html
    url(r'^motor/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        MotorDetail.as_view(),
        name='motor_detail'),
    # Create a brand: /icars/marques/create/
    url(r'^marques/create/$',
        MarcaCreate.as_view(),
        name='brand_create'),
    #Edit a brand: /icars/marques/1/edit/
    url(r'^marques/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        model = Marca,
        template_name='icars/form.html',
        form_class = MarcaForm),
        name='brand_edit'),
    #Create a model: /icars/models/create/
    url(r'^models/create/$',
        ModelCreate.as_view(),
        name='model_create'),
    #Edit a model: /icars/models/1/edit/
    url(r'^models/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        model = Model,
        template_name='icars/form.html',
        form_class = ModelForm),
        name='model_edit'),
    #Create a motor: /icars/motor/create/
    url(r'^motor/create/$',
        MotorCreate.as_view(),
        name='motor_create'),
    #Edit a motor: /icars/motor/1/edit/
    url(r'^motor/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        model = Motor,
        template_name='icars/form.html',
        form_class = MotorForm),
        name='motor_edit'),
    #Create a style: /icars/estil/create/
    url(r'^estil/create/$',
        EstilCreate.as_view(),
        name='style_create'),
    #Edit a model: /icars/estil/1/edit/
    url(r'^estil/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        model = Estil,
        template_name='icars/form.html',
        form_class = EstilForm),
        name='style_edit'),



]

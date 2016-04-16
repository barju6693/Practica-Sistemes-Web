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
    # List all brands: /icars/marques.json
    url(r'^marques\.(?P<extension>(json|xml|html))$',
        MarcaList.as_view(),
        name='marca_list'),
    # List all models: /icars/models.json
    url(r'^models\.(?P<extension>(json|xml|html))$',
        ModelList.as_view(),
        name='model_list'),
    #List 10 styles : /icars/estil.json
    url(r'^estil\.(?P<extension>(json|xml|html))$',
        EstilDetail.as_view(),
        name='new_car_list'),

]

from django.forms import ModelForm
from models import *

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude = ('niceName',)

class ModelForm(ModelForm):
    class Meta:
        model = Model
        exclude = ('niceName', 'state', 'years',)

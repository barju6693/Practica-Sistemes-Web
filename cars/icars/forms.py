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


class MotorForm(ModelForm):
    class Meta:
        model = Motor
        exclude = ('availability',)


class EstilForm(ModelForm):
    class Meta:
        model = Estil
        exclude = ('trim', 'Submodel.niceName',)

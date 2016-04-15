from django.contrib.auth.models import User, Group
from icars.models import Marca, Model, Year, Estil, Motor, Transmission
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField

class ModelSerializer(serializers.HyperlinkedModelSerializer):
    

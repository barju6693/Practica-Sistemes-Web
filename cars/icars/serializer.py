from django.contrib.auth.models import User, Group
from django.core import serializers
from icars.models import Marca, Model, Year, Estil, Motor, Transmission
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField,
HyperlinkedIdentityField

#class ModelSerializer(serializers.HyperlinkedModelSerializer):


class MarcaSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.TextField()
    niceName = serializers.TextField()
    models = []

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('icars:brand_detail', kwargs={'pk': self.pk})


class ModelSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    years = []
    name = serializers.TextField()
    niceName = serializers.TextField()
    state = []

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('icars:model_detail', kwargs={'pk': self.pk})


class YearSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    year = serializers.PositiveSmallIntegerField(default=1)


class EstilSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.TextField()
    trim = serializers.TextField()
    # en aquestes classe interne, no sei si al on delete
    # s'ha de possar serializers o models

    class MakeSerializer:
        id = serializers.ForeignKey(Marca, on_delete=serializers.CASCADE)
        name = serializers.TextField()
        niceName = serializers.TextField()

    class ModelSerializer:
        id = serializers.ForeignKey(Model, on_delete=serializers.CASCADE)
        name = serializers.TextField()
        niceName = serializers.TextField()

    class YearSerializer:
        id = serializers.ForeignKey(Year, on_delete=serializers.CASCADE)
        year = serializers.PositiveSmallIntegerField()

    class SubmodelSerializer:
        body = serializers.TextField()
        fuel = serializers.TextField()
        tuner = serializers.TextField()
        modelName = serializers.TextField()
        niceName = serializers.TextField()


class MotorSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.TextField()
    equipmentType = serializers.TextField(default="ENGINE")
    availability = serializers.TextField()
    compressionRatio = serializers.DecimalField(max_digits=7, decimal_places=5)
    cylinder = serializers.PositiveSmallIntegerField()
    size = serializers.DecimalField(max_digits=7, decimal_places=4)
    displacement = serializers.PositiveSmallIntegerField()
    configuration = serializers.TextField()
    fuelType = serializers.TextField()
    horsePower = serializers.PositiveSmallIntegerField()
    torque = serializers.PositiveSmallIntegerField()
    totalValues = serializers.PositiveSmallIntegerField()
    manufacturerEngineCode = serializers.TextField()
    typeN = serializers.TextField()
    code = serializers.TextField()
    compressorType = serializers.TextField()


class TransmissionSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.TextField()
    equipmentType = serializers.TextField(default="TRANSMISSION")
    availability = serializers.TextField()
    automaticType = serializers.TextField()
    transsmisionType = serializers.TextField()
    numberOfSpeeds = serializers.PositiveSmallIntegerField()

# quan es passa format, ha de ser una string; sera "json" , "xml"


def SerializeObject(serializedObj, format):
    serialized_data = serializers.serialize(format, serializedObj)


def DesserializeObject(serialized_data, format):
    for deserialized_object in serializers.deserialize(format, serialized_data):
        deserialized_object.save()
    return deserialized_object

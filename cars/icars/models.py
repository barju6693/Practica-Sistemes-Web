from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    niceName = models.TextField()
    models = []

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('icars:brand_detail', kwargs={'pk': self.pk})


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    years = []
    name = models.TextField()
    niceName = models.TextField()
    state = []

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('icars:model_detail', kwargs={'pk': self.pk})


class Year(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField(default=1)


class Estil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    trim = models.TextField()

    class Make:
        id = models.ForeignKey(Marca, on_delete=models.CASCADE)
        name = models.TextField()
        niceName = models.TextField()

    class Model:
        id = models.ForeignKey(Model, on_delete=models.CASCADE)
        name = models.TextField()
        niceName = models.TextField()

    class Year:
        id = models.ForeignKey(Year, on_delete=models.CASCADE)
        year = models.PositiveSmallIntegerField()

    class Submodel:
        body = models.TextField()
        fuel = models.TextField()
        tuner = models.TextField()
        modelName = models.TextField()
        niceName = models.TextField()


class Motor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    equipmentType = models.TextField(default="ENGINE")
    availability = models.TextField()
    compressionRatio = models.DecimalField(max_digits=7, decimal_places=5)
    cylinder = models.PositiveSmallIntegerField()
    size = models.DecimalField(max_digits=7, decimal_places=4)
    displacement = models.PositiveSmallIntegerField()
    configuration = models.TextField()
    fuelType = models.TextField()
    horsePower = models.PositiveSmallIntegerField()
    torque = models.PositiveSmallIntegerField()
    totalValues = models.PositiveSmallIntegerField()
    manufacturerEngineCode = models.TextField()
    typeN = models.TextField()
    code = models.TextField()
    compressorType = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('icars:motor_detail', kwargs={'pk': self.pk})


class Transmission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    equipmentType = models.TextField(default="TRANSMISSION")
    availability = models.TextField()
    automaticType = models.TextField()
    transsmisionType = models.TextField()
    numberOfSpeeds = models.PositiveSmallIntegerField()

from django.db import models


# Create your models here.

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    years = []
    name = models.TextField()
    niceName = models.TextField()
    state = []

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    conjuntModels = []
    name = models.TextField()
    niceName = models.TextField()

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

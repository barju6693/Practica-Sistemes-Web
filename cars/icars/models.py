from django.db import models


# Create your models here.

class Model(models.Model):
    iden = models.IntegerField()
    years = []
    name = models.TextField()
    niceName = models.TextField()
    state = []

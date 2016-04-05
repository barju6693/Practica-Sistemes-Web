from django.db import models

# Create your models here.
class model(models.Model):
    id = models.IntegerField()
    years = []
    name = models.TextField()
    niceName = models.TextField()
    state = []


from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)

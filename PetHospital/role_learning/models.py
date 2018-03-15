from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)


class Flow(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
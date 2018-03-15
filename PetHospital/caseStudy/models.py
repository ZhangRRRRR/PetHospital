from django.db import models

# Create your models here.
class DiseaseType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class DiseaseEntity(models.Model):
    name = models.CharField(max_length=200)
    diseaseType = models.ForeignKey(DiseaseType,on_delete = models.CASCADE)

class DiseaseCase(models.Model):
    name = models.CharField(max_length=200)
    diseaseEntity = models.ForeignKey(DiseaseEntity,on_delete = models.CASCADE)

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200)
    diseaseCases = models.ManyToManyField(DiseaseCase)

class Vaccine(models.Model):
    name = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200)
    diseaseCases = models.ManyToManyField(DiseaseCase)

class DiseaseStage(models.Model):
    name = models.CharField(max_length = 200)
    diseaseCase = models.ForeignKey(DiseaseCase,on_delete = models.CASCADE)

class TextInformation(models.Model):
    content  = models.CharField(max_length = 200)
    diseaseStage = models.ForeignKey(DiseaseStage, on_delete = models.CASCADE)

class ImageInformation(models.Model):
    content =  models.CharField(max_length = 200)
    diseaseStage = models.ForeignKey(DiseaseStage, on_delete = models.CASCADE)

class VideoInformation(models.Model):
    content = models.CharField(max_length = 200)
    diseaseStage = models.ForeignKey(DiseaseStage, on_delete = models.CASCADE)

class CheckItem(models.Model):
    name = models.CharField(max_length = 200)
    instruction = models.CharField(max_length = 200)
    testData = models.CharField(max_length = 200)
    normalData = models.CharField(max_length = 200)
    result = models.BooleanField()
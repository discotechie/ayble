from django.db import models
from users.models import CustomUser

class Symptom(models.Model):
    symptom = models.CharField(max_length=100)
    users = models.ManyToManyField(CustomUser, related_name='symptoms')

class Diagnosis(models.Model):
    diagnosis = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom, related_name='diagnoses')
    users = models.ManyToManyField(CustomUser, related_name='diagnoses')

class Food(models.Model):
    food = models.CharField(max_length=100)
    users = models.ManyToManyField(CustomUser, related_name='trigger_foods')
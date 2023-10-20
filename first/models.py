from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
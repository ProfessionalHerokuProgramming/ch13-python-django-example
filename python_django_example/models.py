from django.db import models

class Employee(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

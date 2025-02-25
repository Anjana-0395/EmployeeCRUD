from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
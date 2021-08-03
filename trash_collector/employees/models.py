from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Employee(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    

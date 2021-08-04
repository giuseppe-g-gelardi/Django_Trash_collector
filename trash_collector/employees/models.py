from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employees(models.Model):
    name = models.CharField
    zipcode = models.CharField
    address = models.CharField
    start_date = models.DateField
    end_date = models.DateField
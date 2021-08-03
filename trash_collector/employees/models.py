<<<<<<< HEAD
from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employees(models.Model):
    name = models.CharField
    zipcode = models.CharField
    address = models.CharField
=======
from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Employee(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
>>>>>>> a38f4f1bf4be0db1f5cb0096ff369db5cf1d479f

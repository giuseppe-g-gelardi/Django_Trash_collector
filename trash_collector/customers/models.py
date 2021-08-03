<<<<<<< HEAD
from django.db import models
from django.db.models.fields import DateField, IntegerField
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField
    zipcode = models.CharField
    weekly_pickup_day = models.CharField
    one_time_pickup = models.DateField(null=True)
    balance = models.IntegerField(default=0)
    suspend_start = models.DateField(null=True)
    suspend_end = models.DateField(null=True)
=======
from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

# ! web url -> urls.py -> views.py method -> html file
# ? url -> routes file -> controller file -> view file
>>>>>>> a38f4f1bf4be0db1f5cb0096ff369db5cf1d479f

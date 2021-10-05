from django.db import models
from django.db.models.fields import DateField, IntegerField
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    class PickupDay(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True,on_delete=models.CASCADE)
    address = models.CharField
    zipcode = models.CharField
    weekly_pickup_day = models.CharField
    one_time_pickup = models.DateField(null=True)
    balance = models.IntegerField(default=0)
    suspend_start = models.DateField(null=True)
    suspend_end = models.DateField(null=True)

class AccountInfo(models.Model):
    name = models.CharField(max_length=20)

class BudgetInfo(models.Model):
    user = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    user_budget = models.IntegerField(default=0)
    expenses = models.IntegerField(default=0)
    category = models.CharField



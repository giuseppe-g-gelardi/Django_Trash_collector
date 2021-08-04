# from trash_collector.accounts.models import User
from django.db import reset_queries
from django.db.models.fields.related import ForeignKey
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)

    except:
      
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        pass

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
    print(user)
    return render(request,'customers/index.html')

def weekly_pick_up(request,customers_id ):
    print()
    if request.method == 'POST':
        current_customer = Customer.objects.get(customers_id)
    current_customer = Customer.objects.get(customers_id)
    context = {
        'current_customer': current_customer
    }
    return render(request, "customers/index.html", context)


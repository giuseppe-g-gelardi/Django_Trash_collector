from django.db import reset_queries
from django.db.models.fields.related import ForeignKey
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import BudgetInfo, Customer
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

def weekly_pick_up(request,user ):
    if request.method == 'POST':
        user = request.user
        current_customer = Customer.objects.get(user_id=user.id)
        current_customer.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        current_customer.save()
    current_customer = Customer.objects.get(user.id)
    context = {
        'current_customer': current_customer
    }
    return render(request, "customers/index.html", context)



def one_time_pick_up(request,user ):
    if request.method == 'POST':
        user = request.user
        current_customer = Customer.objects.get(user_id=user.id)
        current_customer.one_time_pickup = request.POST.get('one_time_pickup')
        current_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))    
    current_customer = Customer.objects.get(user.id)
    context = {
        'current_customer': current_customer
    }
    return render(request, "customers/index.html", context)


def account_info(request, user):
    if request.method == 'POST':
        current_customer_account_info = Customer.objects.get(user_id=user.id)
        current_customer_account_info.name = request.POST.get('name')
        current_customer_account_info.user = request.POST.get('user')
        current_customer_account_info.address = request.POST.get('address')
        current_customer_account_info.zipcode = request.POST.get('zipcode')
        current_customer_account_info.weekly_pickup_day = request.POST.get('weekly_pickup_day') 
        current_customer_account_info.suspend_start = request.POST.get('suspend_start') 
        current_customer_account_info.suspend_end = request.POST.get('suspend_end') 
        current_customer_budget_info = BudgetInfo.objects.get(user_id=user.id)
        current_customer_budget_info.user_budget = request.POST.get('user_budget')
        current_customer_budget_info.expenses = request.POST.get('expenses')       
        current_customer_account_info.save()
        return HttpResponseRedirect(reverse('customers:index'))    
    
    current_customer_account_info = Customer.objects.get(user_id=user.id)
    context = {
        'current_customer_account_info': current_customer_account_info
    }
    return render(request, 'customers/index.html', context)

<<<<<<< HEAD
from django.shortcuts import redirect, render


def group_redirect(request):
    """This single view function redirects a user to the customer or employee index if they are in either group"""
    if request.user.groups.filter(name="Customers").exists():
        return redirect('/customers/')
    elif request.user.groups.filter(name="Employees").exists():
        return redirect('/employees/')
    else:
        # If user is in neither group, get sent back to home
        return render(request, 'home.html')
=======
from django.shortcuts import redirect, render


def group_redirect(request):
    """This single view function redirects a user to the customer or employee index if they are in either group"""
    if request.user.groups.filter(name="Customers").exists():
        return redirect('/customers/')
    elif request.user.groups.filter(name="Employees").exists():
        return redirect('/employees/')
    else:
        # If user is in neither group, get sent back to home
        return render(request, 'home.html')
>>>>>>> a38f4f1bf4be0db1f5cb0096ff369db5cf1d479f

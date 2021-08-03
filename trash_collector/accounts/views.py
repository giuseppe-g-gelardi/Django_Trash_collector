<<<<<<< HEAD
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUserForm


class RegisterView(generic.CreateView):
    """Allows user to register with the custom form we created"""
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
=======
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUserForm


class RegisterView(generic.CreateView):
    """Allows user to register with the custom form we created"""
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
>>>>>>> a38f4f1bf4be0db1f5cb0096ff369db5cf1d479f

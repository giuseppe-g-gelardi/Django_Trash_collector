<<<<<<< HEAD
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]
=======
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]
>>>>>>> a38f4f1bf4be0db1f5cb0096ff369db5cf1d479f

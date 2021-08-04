from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:customer_id>/',views.weekly_pick_up,name='weekly_pick_up')
]


# ! web url -> urls.py -> views.py method -> html file
# ? url -> routes file -> controller file -> view file
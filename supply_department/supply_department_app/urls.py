from django.urls import path
from . import views

app_name = "supply_department_app"

urlpatterns = [
    path('', views.index, name="index"),
]

from turtle import home
from django.urls import path
from HR_Department import views



urlpatterns = [
    #path("", views.home, name="home"),
        # Replace the existing path for ""
    path("Employee_list/", views.Employee_list, name="Employees"),
    path("Data_Input/", views.Data_Input, name="Employees_details"),
]

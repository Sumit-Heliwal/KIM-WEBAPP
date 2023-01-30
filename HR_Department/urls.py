from turtle import home
from django.urls import path
from HR_Department import views



urlpatterns = [
    #path("", views.home, name="home"),
        # Replace the existing path for ""
    path("Employee_list/", views.Employee_list, name="Employees"),
    path("Data_Input/", views.Data_Input, name="Employees_details"),
    path('Add_Employee/', views.add_Employee, name='add_Employee'),
    path('Add_Employee_Code/', views.add_Employee_code, name='add_Employee_code'),
    path("Search_cd/", views.search_view_name, name="search_cd"),
    path('edit/<int:id>', views.edit, name="edit"),  
    path('update/<int:id>', views.update, name="update"), 
]

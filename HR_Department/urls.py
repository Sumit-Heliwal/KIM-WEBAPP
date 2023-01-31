from turtle import home
from django.urls import path
from HR_Department import views



urlpatterns = [
    #path("", views.home, name="home"),
        # Replace the existing path for ""
  
    path("Employee_list/", views.Employee_code_list, name="view_Employee_code"),
    path('Add_Employee_Code/', views.add_Employee_code, name='add_Employee_code'),
    path("Search_Employee_code/", views.search_Employee_code, name="search_Employee_code"),
    path('edit_Employee_code/<int:id>', views.edit_Employee_code, name="edit_Employee_code"),  
    path('update_Employee_code/<int:id>', views.update_Employee_code, name="update_Employee_code"), 
    
    path("Employees_details/", views.Employees_details, name="Employees_details"),
    path('Add_Employee/', views.add_Employee, name='add_Employee'),
    path("Search_Employee_details/", views.search_Employee_details, name="search_Employee_details"),
    path('edit_Employee_details/<int:id>', views.edit_Employee_details, name="edit_Employee_details"),  
    path('update_Employee_details/<int:id>', views.update_Employee_details, name="update_Employee_details"), 
]

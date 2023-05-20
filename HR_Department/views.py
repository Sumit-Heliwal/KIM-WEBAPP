import json
from datetime import datetime
from .models import Reporting_Officer, Employee_Data
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Add these to existing imports at the top of the file:


#def home(request):
#    return HttpResponse("Hello, Django!")
# Replace the existing home function with the one below


def Employee_code_list(request):
    title ="Employee Code"
    data = Reporting_Officer.objects.values()
    return render(request, "Studentdata/student.html" , {'data': data , 'title':title})

def add_Employee_code(request):
    title ="Add Employee Code"
    form = Add_Employee_code(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect("view_Employee_code") 
    return render(request, "Studentdata/input_data.html" , {'data': form , 'title':title})


def search_Employee_code(request):
    title ="Search"
    if request.method == 'POST':
        searchobj = request.POST.get('name')
        if(Reporting_Officer.objects.filter(Emp_Code=searchobj).exists()):
            obj = Reporting_Officer.objects.filter(Emp_Code = searchobj)
            a = True
            return render(request,'Studentdata/forms_search_employee_code.html' ,{'title' : title , 'data' : obj , 'a' : a})     
        else:
            errors = 'Invalid Employee_code'
            a = False
            return render(request,'Studentdata/forms_search_employee_code.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "Studentdata/forms_search_employee_code.html", {'title' : title})
        
        # form = Add_Employee_code(request.POST or None)
        # if request.method == 'POST':
        #     searchobj = request.POST.get('name')
            
        #     if(Reporting_Officer.objects.filter(Emp_Code=searchobj).exists()):
        #         obj = Reporting_Officer.objects.get(Emp_Code = searchobj)
        #         a = True
        #         form = Add_Employee_code(instance= obj)
        #         return render(request,'Studentdata/forms_search_employee_code.html' ,{'title' : title , 'obj' : obj , 'a' : a ,'data': form })     
        #     else:
        #         errors = 'Invalid Name'
        #         a = False
        #         return render(request,'Studentdata/forms_search_employee_code.html' ,{'title' : title , 'errors': errors , 'a' : a , 'data': form})     
        # return render( request, "Studentdata/forms_search_employee_code.html", {'title' : title})
          
def edit_Employee_code(request, id):  
    title = 'Edit'
    employee = Reporting_Officer.objects.get(Emp_Code = id)  
    form = Add_Employee_code(instance = employee)  

    return render(request,'Studentdata/edit_employee_code.html', {'data':form , "id" : id, 'title': title})  


def update_Employee_code(request, id):
    title = "Update"  
    employee = Reporting_Officer.objects.get(Emp_Code = id)  
    form = Add_Employee_code(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("view_Employee_code") 
    else:
        errors = "Error Occured! Can be a Duplicate Name"
        return render(request,'Studentdata/edit_employee_code.html' , {'data': form, "id" : id ,'errors': errors , 'title': title}) 
    
#############################  Employee Details   #########################################################
    
def Employees_details(request):
    title ="Employee Data"
    data = Employee_Data.objects.values()
    return render(request, "Studentdata/student.html" , {'data': data , 'title':title})

def add_Employee(request):
    title ="Add Employee"
    form = Add_Employee(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect("Employees_details") 
    return render(request, "Studentdata/input_data.html" , {'data': form , 'title':title})
            
def search_Employee_details(request):
    title ="Search"
    if request.method == 'POST':
        searchobj = request.POST.get('name')
        if(Employee_Data.objects.filter(Emp_Code = searchobj).exists()):
            obj = Employee_Data.objects.filter(Emp_Code = searchobj)
            for each in obj:
                data = str(each.Emp_Code) 
            code = data[:4]              
            a = True
            return render(request,'Studentdata/forms_search_employee_data.html' ,{'title' : title , 'code' : code , 'data':obj, 'a' : a})     
        else:
            errors = 'Invalid Employee_code'
            a = False
            return render(request,'Studentdata/forms_search_employee_data.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "Studentdata/forms_search_employee_data.html", {'title' : title})
    

def edit_Employee_details(request, id):  
    title = 'Edit'
    employee = Employee_Data.objects.get(Emp_Code = id)  
    form = Add_Employee(instance = employee)  

    return render(request,'Studentdata/edit_employee_data.html', {'data':form , "id" : id, 'title': title})  


def update_Employee_details(request, id):
    title = "Update"  
    employee = Employee_Data.objects.get(Emp_Code = id)  
    form = Add_Employee(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("view_Employee_code") 
    else:
        errors = "Error Occured! Can be a Duplicate Name"
        return render(request,'Studentdata/edit_employee_data.html' , {'data': form, "id" : id ,'errors': errors , 'title': title}) 
    

################## Employee Education Data ############################

def Employees_Education(request):
    title ="Employee Data"
    data = Employee_Data.objects.values()
    return render(request, "Studentdata/student.html" , {'data': data , 'title':title})

def add_Employees_Education(request):
    title ="Add Employee"
    form = Add_Employee(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect("Employees_details") 
    return render(request, "Studentdata/input_data.html" , {'data': form , 'title':title})
            
def search_Employees_Education(request):
    title ="Search"
    if request.method == 'POST':
        searchobj = request.POST.get('name')
        if(Employee_Data.objects.filter(Emp_Code = searchobj).exists()):
            obj = Employee_Data.objects.filter(Emp_Code = searchobj)
            for each in obj:
                data = str(each.Emp_Code) 
            code = data[:4]              
            a = True
            return render(request,'Studentdata/forms_search_employee_data.html' ,{'title' : title , 'code' : code , 'data':obj, 'a' : a})     
        else:
            errors = 'Invalid Employee_code'
            a = False
            return render(request,'Studentdata/forms_search_employee_data.html' ,{'title' : title , 'errors': errors , 'a' : a})     
    return render( request, "Studentdata/forms_search_employee_data.html", {'title' : title})
    

def edit_Employees_Education(request, id):  
    title = 'Edit'
    employee = Employee_Data.objects.get(Emp_Code = id)  
    form = Add_Employee(instance = employee)  

    return render(request,'Studentdata/edit_employee_data.html', {'data':form , "id" : id, 'title': title})  


def update_Employees_Education(request, id):
    title = "Update"  
    employee = Employee_Data.objects.get(Emp_Code = id)  
    form = Add_Employee(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("view_Employee_code") 
    else:
        errors = "Error Occured! Can be a Duplicate Name"
        return render(request,'Studentdata/edit_employee_data.html' , {'data': form, "id" : id ,'errors': errors , 'title': title}) 
    




# def contact(request):
#     return render(request, "Studentdata/contact.html")


# # You can also remove the import re statement that's no longer used

# def hello_there(request, name):
#     return render(
#         request,
#         'Studentdata/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )

# Add this code elsewhere in the file:
# def log_message(request):
#     form = LogMessageForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.log_date = datetime.now()
#             message.save()
#             return redirect("home")
#     else:
#         return render(request, "hello/log_message.html", {"form": form})
    
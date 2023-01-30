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


def Employee_list(request):
    title ="Employee Code"
    data = Reporting_Officer.objects.values()
    return render(request, "Studentdata/student.html" , {'data': data , 'title':title})

def Data_Input(request):
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
    return render(request, "Studentdata/input_data.html" , {'data': form , 'title':title})

def add_Employee_code(request):
    title ="Add Employee Code"
    form = Add_Employee_code(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
    return render(request, "Studentdata/input_data.html" , {'data': form , 'title':title})


def search_view_name(request):
        title ="Search"
        if request.method == 'POST':
                searchobj = request.POST.get('name')
                if(Reporting_Officer.objects.filter(Emp_Code=searchobj).exists()):
                    obj = Reporting_Officer.objects.filter(Emp_Code = searchobj)
                    a = True
                    return render(request,'Studentdata/forms_search.html' ,{'title' : title , 'data' : obj , 'a' : a})     
                else:
                    errors = 'Invalid Name'
                    a = False
                    return render(request,'Studentdata/forms_search.html' ,{'title' : title , 'errors': errors , 'a' : a})     
        return render( request, "Studentdata/forms_search.html", {'title' : title})
        
        # form = Add_Employee_code(request.POST or None)
        # if request.method == 'POST':
        #     searchobj = request.POST.get('name')
            
        #     if(Reporting_Officer.objects.filter(Emp_Code=searchobj).exists()):
        #         obj = Reporting_Officer.objects.get(Emp_Code = searchobj)
        #         a = True
        #         form = Add_Employee_code(instance= obj)
        #         return render(request,'Studentdata/forms_search.html' ,{'title' : title , 'obj' : obj , 'a' : a ,'data': form })     
        #     else:
        #         errors = 'Invalid Name'
        #         a = False
        #         return render(request,'Studentdata/forms_search.html' ,{'title' : title , 'errors': errors , 'a' : a , 'data': form})     
        # return render( request, "Studentdata/forms_search.html", {'title' : title})
   
def edit(request, id):  
    employee = Reporting_Officer.objects.get(Emp_Code = id)  
    form = Add_Employee_code(instance = employee)  

    return render(request,'Studentdata/edit.html', {'data':form , "id" : id})  


def update(request, id):  
    employee = Reporting_Officer.objects.get(Emp_Code = id)  
    form = Add_Employee_code(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("Employees") 
    else:
        errors = "Error Occured! Can be a Duplicate Name"
        return render(request,'Studentdata/edit.html' , {'data': form, "id" : id ,'errors': errors}) 
    return render(request, 'Studentdata/edit.html', {'data': form, "id" : id})  
    
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
    
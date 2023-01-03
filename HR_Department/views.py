import json
from django.shortcuts import render
from datetime import datetime
from .models import Reporting_Officer, Employee_Data

# Add these to existing imports at the top of the file:


#def home(request):
#    return HttpResponse("Hello, Django!")
# Replace the existing home function with the one below


def Employee_list(request):
    data = Reporting_Officer.objects.values()
    return render(request, "Studentdata/student.html" , {'data': data})

def Data_Input(request):
    data = Employee_Data.objects.values()
    return render(request, "Studentdata/hostel.html" , {'data': data})

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
    
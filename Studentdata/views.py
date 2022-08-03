from django.shortcuts import render
from datetime import datetime
# Add these to existing imports at the top of the file:


#def home(request):
#    return HttpResponse("Hello, Django!")
# Replace the existing home function with the one below
def home(request):
   return render(request, "Studentdata/home.html")
# Remove the old home function if you want; it's no longer used

def about(request):
    return render(request, "Studentdata/about.html")

def contact(request):
    return render(request, "Studentdata/contact.html")


# You can also remove the import re statement that's no longer used

def hello_there(request, name):
    return render(
        request,
        'Studentdata/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

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
    
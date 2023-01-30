from turtle import home
from django.urls import path
from Studentdata import views



urlpatterns = [
    path("", views.home, name="home"),
        # Replace the existing path for ""
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("student/", views.student, name="student"),
    path("hostel/", views.hostel, name="hostel"),
    path("contact/", views.contact, name="contact"),

]

from operator import mod
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Roll_No =  models.CharField(max_length= 12, primary_key=True)
    Batch =models.CharField(max_length=5)
    Contect_No = models.BigIntegerField()
    Email_ID = models.EmailField()
    College_Email_ID = models.EmailField()
    Address = models.CharField(max_length=300)
    DOB = models.DateField()
    Campus = models.CharField(max_length=10)
    Major = models.CharField(max_length=15)
    Minor = models.CharField(max_length=15)
    SSC = models.CharField(max_length=5)
    School = models.CharField(max_length=50)
    HSC = models.CharField(max_length=5)
    Jr_College = models.CharField(max_length=50)
    Graduation = models.CharField(max_length=5)
    Sr_College = models.CharField(max_length=50)
    Graduation_Branch = models.CharField(max_length=25)
    Masters = models.CharField(max_length=5)
    Masters_Branch = models.CharField(max_length=25)
    Masters_University = models.CharField(max_length=50)
    
FLOOR_CHOICES = (
    ("Ground", "Ground"),
    ("First", "First"),
    ("Second", "Second"),
)

class Hostel(models.Model):
    Roll_No = models.ForeignKey(Student, on_delete=models.CASCADE)
    Room_No = models.CharField(max_length=3)
    Floor = models.CharField(max_length=6, choices=FLOOR_CHOICES, default="Ground")
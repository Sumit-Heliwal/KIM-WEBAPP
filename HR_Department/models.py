from django.db import models

# Create your models here.

Blood_group = (
    ("A +ve", "A +ve"),
    ("A -ve", "A -ve"),
    ( "B +ve", "B +ve"),
    ( "O +ve", "O +ve"),
    ( "AB +ve", "AB +ve"),
    ( "B -ve", "B -ve"),
    ( "O -ve", "O -ve"),
    ( "AB -ve", "AB -ve"),
    
)

class Employee_Data(models.Model):
    Emp_Code = models.CharField(max_length= 12, primary_key=True)
    Employee_Name = models.CharField(max_length=100, unique=True)
    Designation = models.CharField(max_length=25)
    Address_1 = models.CharField(max_length=300)
    Address_2 = models.CharField(max_length=300)
    Contact_no1 = models.BigIntegerField()
    Contact_no2 = models.BigIntegerField()
    Personal_Email_ID =  models.EmailField()
    Official_Email_ID =  models.EmailField()
    Date_of_Birth = models.DateField()
    Date_of_Joining = models.DateField()
    Date_of_Confirmation = models.DateField()
    Blood_Group =models.CharField(max_length=6, choices=Blood_group, default="A +ve")



class Leave_Data(models.Model):
    Emp_Code = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    Leave_Type = models.CharField(max_length=25)
    From_Date = models.DateField()
    To_Date = models.DateField()
    Recommended_Authority = models.ForeignKey(Employee_Data, related_name='RECOMENDED_AYTHORITY' ,on_delete=models.CASCADE)
    Approved_By = models.ForeignKey(Employee_Data, related_name='APPROVED_BY', on_delete=models.CASCADE)
    Reason_for_Leave = models.CharField(max_length=300)
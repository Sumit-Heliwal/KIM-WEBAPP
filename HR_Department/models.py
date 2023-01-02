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
class Reporting_Officer(models.Model):
    Emp_Code = models.CharField(max_length= 4, primary_key=True)
    Employee_Name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
         return (self.Emp_Code + ", " + self.Employee_Name )
    
     
class Employee_Data(models.Model):
    Emp_Code = models.ForeignKey(Reporting_Officer, on_delete=models.CASCADE)
    Emp_type = models.TextChoices('Emp_type', 'Teaching Non_Teaching')
    Emp_Type = models.CharField(max_length=15, choices=Emp_type.choices, default="Non_Teaching")
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
    Reporting_Authority = models.ForeignKey(Reporting_Officer,related_name='Reporting_Authority', on_delete=models.CASCADE, default='1111')
    
    


class Leave_Data(models.Model):
    Emp_Code = models.ForeignKey(Reporting_Officer, on_delete=models.CASCADE)
    Leave_Type = models.CharField(max_length=25)
    From_Date = models.DateField()
    To_Date = models.DateField()
    Recommended_Authority = models.ForeignKey(Reporting_Officer, related_name='RECOMENDED_AYTHORITY' ,on_delete=models.CASCADE)
    Approved_By = models.ForeignKey(Reporting_Officer, related_name='APPROVED_BY', on_delete=models.CASCADE)
    Reason_for_Leave = models.CharField(max_length=300)
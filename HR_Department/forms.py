from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'


class Add_Employee(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Employee_Data
        fields = "__all__"

# class Product(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Add_Product
#         fields = ['Product_Name']


# class Sale_Form(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Customer_Sale
#         fields = "__all__"
#         widgets = {
#             'Sale_Date': DateInput(),
#             'Payment_Date': DateInput()
#         }


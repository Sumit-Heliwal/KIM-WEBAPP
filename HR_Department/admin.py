from django.contrib import admin

# Register your models here.
from .models import Employee_Data, Leave_Data

admin.site.register(Employee_Data)
admin.site.register(Leave_Data)
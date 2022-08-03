from django.contrib import admin

# Register your models here.
from .models import Hostel,Student

admin.site.register(Student)
admin.site.register(Hostel)

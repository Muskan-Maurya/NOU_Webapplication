from django.contrib import admin
from .models import Student, Login,Enquiry

# Register your models here.
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Enquiry)
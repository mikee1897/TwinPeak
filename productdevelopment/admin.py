from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Customer_Contact_Person)
admin.site.register(Customer_Landline_Number)
admin.site.register(Customer_Mobile_Number)
admin.site.register(Customer_Email)
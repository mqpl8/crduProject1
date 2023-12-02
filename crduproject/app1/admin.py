from django.contrib import admin
from .models import  MyUser,Books

# Register your models here.

admin.site.register(Books)
admin.site.register(MyUser)


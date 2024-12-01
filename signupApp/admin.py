from django.contrib import admin
from . models import *

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id','name','address','password','email','contact','age','dob','gender','language','qualification']
admin.site.register(Signup,SignupAdmin)
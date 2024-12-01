from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    contact =models.IntegerField
    age=models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    qualigication =models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
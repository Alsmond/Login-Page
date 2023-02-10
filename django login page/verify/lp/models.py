from django.db import models

# Create your models here.
class Login(models.Model):
    Name=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=10,null=False,blank=False)
    
def __str__(self):
    return self.Name

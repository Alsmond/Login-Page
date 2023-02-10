from django.shortcuts import render
from .models import Login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login (request):
    if request.method=='POST':
        name=request.POST.get('name')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(name,lname,email,password)
        l=Login(Name=name,Lname=lname,Email=email,Password=password)
        l.save()
        messages.success(request,"you have successfully loged in")
    
        
    
    return render(request,'login.html')
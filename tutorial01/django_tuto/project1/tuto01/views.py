from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'tuto01/index.html')

def login(request):
    data = request.POST.get('data')
    return render(request,'tuto01/login.html',{'data':data})
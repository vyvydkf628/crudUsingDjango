from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'board/index.html')


def create(request):
    return render(request,'board/create.html')


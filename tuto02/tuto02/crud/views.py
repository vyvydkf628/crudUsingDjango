from django.shortcuts import render,redirect
from .models import Board
# Create your views here.


def index(request):
    boards= Board.objects.all()
    return render(request,'crud/index.html',{'boards':boards})

def new(request):
    
    return render(request,'crud/new.html')
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title,content=content)
    board.save()
    return redirect('/crud/')

def detail(request,pk):
    board = Board.objects.get(pk=pk)

    return render(request,'crud/detail.html',{'board': board})
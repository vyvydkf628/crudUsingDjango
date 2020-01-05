from django.shortcuts import render,redirect
from .models import Board
# Create your views here.

def index(request):
    boards= Board.objects.all()

    return render(request,'boards/index.html',{'boards':boards})


def new(request):
    if request.method =='POST':
        board = Board()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail',board.pk)

    else:
        return render(request,'boards/new.html')

def detail(request,boards_pk):
    board= Board.objects.get(pk=boards_pk)
    return render(request,'boards/detail.html',{'board':board})

def delete(request,boards_pk):
    board = Board.objects.get(pk=boards_pk)
    board.delete()
    return redirect('boards:index')

def edit(request,boards_pk):
    board = Board.objects.get(pk=boards_pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail',board.pk)
    else:
        return render(request,'boards/edit.html',{'board':board})
    
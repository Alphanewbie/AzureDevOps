from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'pages/index.html', context)


def new(request):
    return render(request, 'pages/new.html')


def create(request):
    if(request.method == 'POST'):
        title = request.POST.get("title")
        contents = request.POST.get("contents")

        board = Board(title=title, contents=contents)
        board.save()
        return redirect('pages:index')
    else:
        return render(request, 'pages/new.html')


def detail(request, index):
    board = Board.objects.get(pk=index)
    context = {
        'board': board,
    }
    return render(request, 'pages/detail.html', context)


def delete(request, index):
    if request.method == 'POST':
        board = Board.objects.get(pk=index)
        board.delete()
        return redirect('pages:index')
    else:
        return redirect('pages:detail',index)


def edit(request, index):
    board = Board.objects.get(pk=index)
    context = {
        'board': board,
    }
    return render(request, 'pages/edit.html', context)


def update(request, index):
    if request.method == 'POST':
        board = Board.objects.get(pk=index)
        title = request.POST.get('title')
        contents = request.POST.get('contents')

        board.title = title
        board.contents = contents
        board.save()
        return redirect('pages:detail',index)
    else:
        return redirect('pages:index')

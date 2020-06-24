from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
# 이 데코레이터는 로그인 안하면 자동으로 로그인 페이지로 보낸다.
@login_required
def index(request):
    form = TodoForm()
    todos = Todo.objects.all()
    context = {
        'form' : form,
        'todos' : todos, 
    }
    return render(request,'todo/index.html', context)


@login_required
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        # commit=False : 작업을 확정 시키지 않겠다는 뜻
        todo = form.save(commit=False)
        # 유저 정보는 아티클과 다르게 그냥 request에서 뽑아서 넣으면 된다.
        todo.user = request.user
        todo.save()
        return redirect('todo:index')


@require_POST
@login_required
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    
    todo.delete()
    return redirect('todo:index')
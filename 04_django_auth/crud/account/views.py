from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 장고는 알아서 아이디 테이블이 생성된다.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('account:login')
        pass
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 폼 안의 유저 데이터를 가지고 온다.
            auth_login(request, form.get_user())
            return redirect('todo:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'account/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('account:login')
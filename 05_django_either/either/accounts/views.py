from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login

# https://docs.djangoproject.com/en/3.0/howto/custom-model-fields/
# Create your views here.
def signup(request):
    # 로그인 되어 있는 상태로 접근하면 index로 보낸다.
    if request.user.is_authenticated:
        return redirect('questions:index')

    if request.method == 'POST':
        # 크리에션 폼 덮어 씌웠으니 custom으로 바꿔준다.
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('questions:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('questions:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    return;
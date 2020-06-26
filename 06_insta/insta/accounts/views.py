from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, user_name):
    User = get_user_model()
    user_profile = get_object_or_404(get_user_model(), username=user_name)
    print(user_profile.follow.all())
    context = {
        'user_profile' : user_profile,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    me = request.user
    you = get_object_or_404(get_user_model(), pk=user_pk)
    if me == you:
        return redirect('posts:index')

    # 밑에 주석으로 달린거 둘다 비슷하게 작동한다.
    if me in you.follow.all():
    # if you in me.follower.all():
        # 이미 팔로우 하고 있었음
        # you.follower.remove(me)
        me.follow.remove(you)
    else:
        # 아직 팔로우 안함
        # you.follower.all(me)
        me.follow.add(you)

    return redirect('accounts:profile', you.username)
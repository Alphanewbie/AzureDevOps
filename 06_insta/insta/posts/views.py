from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html')

# 로그인을 안했으면 로그인 페이지로 보내버린다.
@login_required
def create(request):
    if request.method == 'POST':
        # POST요총을 보면 POST안에 File이 없는 것을 알 수 있다. File 은 request안에 따로 별도로 관리 된다.
        # 이대로 하면 루트 디렉토리에 저장된다. setting에 설정
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)

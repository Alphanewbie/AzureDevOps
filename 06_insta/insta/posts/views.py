from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

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


@login_required
def like(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    # user.like_posts => user가 좋아요 버튼을 누른 게시물들
    # post.like_user => post에 좋아요 버튼을 누른 유저들

    if post in user.like_posts.all():
        # 이미 누른 경우
        user.like_posts.remove(post)
        pass
    else:
        # 좋아요 버튼을 아직 안 누른 경우
        user.like_posts.add(post)
        pass
    
    return redirect('posts:index')
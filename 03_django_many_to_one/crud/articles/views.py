from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: 
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'article': article,
        'form' : form,
    }
    
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index') 


@require_POST
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    # content = request.POST.get('content')
    # Comment.objects.create(article=article, content=content)

    form = CommentForm(request.POST)
    # 유효성을 검사를 위해서 만들었다고 보면 된다.
    # 모델폼의 장점 - 유효성검사를 해준다.
    if form.is_valid() :
        # commit=False 입력은 되어있지만 저장은 안한상태(객체만 만들어진 상태)
        # 즉, git으로 보면 add만 되어 있고 commit은 안되있는 상태
        comment = form.save(commit=False)
        # 만들어진 객체에 데이터를 집어 넣는다.
        comment.article = article
        comment.save()

    return redirect('articles:detail', pk)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)

    comment.delete()
    return redirect('articles:detail', article_pk)

from django.shortcuts import render, redirect
# Article.objects를 위해 import 한다.
from .models import Article

# Create your views here.


def index(request):
    # 데이터 베이스에서 모든 값을 뽑아온다.
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 1. new에서 보낸 데이터 받기
    # CSRF 검증에 실패했습니다. 요청을 중단하였습니다.
    # POST의 경우에는 보통 데이터베이스에 조작을 가하기 때문에 최소한의 신원확인이 필수이다.
    title = request.POST.get('title')
    contetn = request.POST.get('contetn')

    # 2. db에 저장
    # article = Article()
    # article.title = title
    # article.contetn = contetn
    # article.save()

    article = Article(title=title, contetn=contetn)
    # 데이터가 유효한지 검사
    # 데이터를 저장할 타이밍이 나온다.
    article.save()
    article.pk
    # 이건 데이터를 저장할 시간이 안나온다. 그래서 잘 안쓰임
    # Article.objects.create(title=title, contetn=contetn)

    # return render(request, 'articles/index.html')
    return redirect('articles:detail', article.pk)
    # return redirect('articles:index')


def detail(request, pk):
    # 뒤에있는 값으로 찾는다.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects. get(pk=pk)
    article.delete()

    return redirect('articles:index')
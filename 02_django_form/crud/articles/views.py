from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # POST라는 것은 서버가 이야기 할때 데이터 베이스를 조작한다는 의미이다.
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        # 유효성 검사
        # models.py의 각각의 값이 맞는지 예를 들면 '',NULL, cruf 토큰이 왔는지 아닌지.
        # 그리고 maxlength 만큼 정해진 대로 됬는가.
        # 만약 Flase라면 유효성 검사가 실패한 이유도 같이 넣어서 Flase리턴이 된다.
        if form.is_valid() :
            # 저장하는 리턴값을 그대로 받아서 보내는 장소를 알려준다.
            article= form.save()
            return redirect('articles:detail', article.pk)
    # 하필 포스트로 나누는 이유. POST가 아닌 method 전부
    # 나머지는 데이터 베이스 조작이 아니라 그냥 뷰만 보여주면 된다는 의미이다.
    else : 
        form = ArticleForm()

    # 이걸 밖으로 빼는 이유 : if form.is_valid() :에서 false가 된다면 return 값이 없게 된다.
    # 그리고 context에 form = ArticleForm(request.POST)을 넣어주기 위해서.
    context = {
        # form의 2가지 모습
        # 1. is_valid()에서 통과하지 못한 form(에러메세지를 포함한다.)
        # 2. else 구문의 form
        'form' : form
    }
    return render(request, 'articles/new.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk) :
    article = Article.objects.get(pk=pk)
    # 작성할꺼면 아래부터 작성하자.
    # 왜냐면 순서대로 생각하기 위해서
    # GET으로 받아서 POST를 반환받기 위해서
    if request.method == 'POST':
        # instance=article을 쓰는 이유 이걸 안 써주면 새로운 인스턴스로 인식해서 새로 글이 써진다.
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid() :
            # 저장하는 리턴값을 그대로 받아서 보내는 장소를 알려준다.
            article= form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 이전의 내용을 출력시켜주기 위해서 빈 form이 아니라 내용을 채워서 보낸다.
        # instance라는 매개변수로 article이라는 값을 넣어준다.
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
    }
    return render(request,'articles/update.html', context)


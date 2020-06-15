from django.shortcuts import render
# Article.objects를 위해 import 한다.
from .models import Article

# Create your views here.
def index(request):
    # 데이터 베이스에서 모든 값을 뽑아온다.
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)

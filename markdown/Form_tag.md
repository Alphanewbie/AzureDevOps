1. `forms.py` 파일 생성

### form 태그 정의
- 내용 : 
```python
from django import forms

# 폼 형태로 정의되어 있는 방법
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20)
    # 텍스트 필드 속성은 없으므로 widget속성의 텍스트 에이리어를 사용한다.
    # widget은 참고
    # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/#widgets-handling-input-of-text
    title = forms.CharField(widget=forms.Textarea)
```

### Model form 태그 정의
- 내용 :
``` python
from django import forms
from .models import Article

# 이건 모델 폼으로 작성하는 방법이다
# 모델에 정의 되어 있는 것을 그대로 활용한다.
class ArticleForm(forms.ModelForm) :
    # title에 어떤 속성을 줄것인가를 명시하는 내용
    # 즉, 옵션이다. 주지 않아도 되는 항목들
    title = forms.CharField(
        label = '제목',
        # 속성을 주는 방법
        # widget은 폼이나 모델폼 두 경우 모두 가능하다
        widget=forms.TimeInput(
            attrs= {
                'class' : 'my-title',
                'placeholder' : 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs= {
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'cols': 50,
                'rows': 5,
            }
        )
    )
    # 데이터에 대한 정보
    # 즉, ArticleForm에 대한 정보
    class Meta :
        model = Article
        # 2 개릐 형식을 사용한다는 의미이다.
        # fields = ['title', 'content',]
        # 모든 value를 가져오려면 all을 사용한다.
        # 단, 입력 가능한 형식만 받기 때문에
        fields = '__all__'

        # 타이틀만 빼고 나머지를 출력하겠다는 의미이다.
        # exclude = ['title']
```

### View.py 수정
- new와 create를 합친다.
    - POST로 입력 받았을때, 등록하는 것으로하고 그 외의 방식은 전부 입력 폼을 보여준다.
```python
def create(request):
    # POST라는 것은 서버가 이야기 할때 데이터 베이스를 조작한다는 의미이다.
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        # models.py의 각각의 값이 맞는지 예를 들면 '',NULL, cruf 토큰이 왔는지 아닌지.
        # 그리고 maxlength 만큼 정해진 대로 됬는가.
        # 만약 Flase라면 유효성 검사가 실패한 이유도 같이 넣어서 Flase리턴이 된다.
        if form.is_valid():
            # 저장하는 리턴값을 그대로 받아서 보내는 장소를 알려준다.
            # 먼약 폼을 사용하면
            # title = form.cleaned_data.get('title')
            # contents = form.cleaned_data.get('contents')
            # 이런 방식으로 하여야 한다.
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 하필 포스트로 나누는 이유. POST가 아닌 method 전부
    # 나머지는 데이터 베이스 조작이 아니라 그냥 뷰만 보여주면 된다는 의미이다.
    else:
        form = ArticleForm()

    # 이걸 밖으로 빼는 이유 : if form.is_valid() :에서 false가 된다면 return 값이 없게 된다.
    # 그리고 context에 form = ArticleForm(request.POST)을 넣어주기 위해서.
    context = {
        # form의 2가지 모습
        # 1. is_valid()에서 통과하지 못한 form(에러메세지를 포함한다.)
        # 2. else 구문의 form
        'form': form
    }
    return render(request, 'articles/new.html', context)
```

### new.html수정방법
- form을 만드는 3가지 방법
```django
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {# https://docs.djangoproject.com/en/3.0/topics/forms/#working-with-form-templates #}
  <h3>Version 1</h3>
  <p>{{ form.as_p }}</p>
  <hr>
  <h3>Version 2</h3>
  <div>
    {{ form.title.errors }}
    {{ form.title.tag }}
    {{ form.title }}
  </div>
  <div>
    {{ form.content.errors }}
    {{ form.content.tag }}
    {{ form.content }}
  </div>
  <h3>Version 3</h3>
  <p>
  {% for field in form %}
    <p>{{ field.error }}</p>
    <p>{{ field.label_tag }}</p>
    <p>{{ field }}</p>
  {% endfor %}
  
  <button class="btn btn-primary">작성</button>
</form>
```

### 부트스트랩 적용 방법
#### 라이브러리 방법
- https://pypi.org/project/django-bootstrap4/

1. `pip install django-bootstrap4`
2. `setting.py`의 `INSTALLED_APPS`에 `'bootstrap4',`를 추가한다.
3. `base.html`의 최 상단에 `{% load bootstrap4 %}`을 추가한다. (`<!DOCTYPE html>`위에)
4. 부트스트랩을 쓰는 html전부 마찬가지로 `{% load bootstrap4 %}`를 추가한다.

#### 평범하게 부트스트랩 쓰는 방법
- 그냥 위젯에 추가해 주는 방식이다.
```python
class ArticleForm(forms.ModelForm) :
    title = forms.CharField(
        label = '제목',
        widget=forms.TimeInput(
            attrs= {
                'class' : 'my-title form-contol',
                ....
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs= {
                'class': 'my-content form-control',
                ....
            }
        )
    )

    class Meta :
        ....
```
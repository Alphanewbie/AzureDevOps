from django import forms
from .models import Article

# Create your models here.
# 폼 형태로 정의되어 있는 방법
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     # 텍스트 필드 속성은 없으므로 widget속성의 텍스트 에이리어를 사용한다.
#     # widget은 참고
#     # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/#widgets-handling-input-of-text
#     title = forms.CharField(widget=forms.Textarea)

# 이건 모델 폼으로 작성하는 방법이다
# 모델에 정의 되어 있는 것을 그대로 활용한다.
class ArticleForm(forms.ModelForm) :
    # title에 어떤 속성을 줄것인가를 명시하는 내용
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
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'cols' : '50',
                'row' : '30',
            }
        )
    )
    # 데이터에 대한 정보
    # 즉, ArticleForm에 대한 정보
    class Meta :
        model = Article
        # 2 개릐 형식을 사용한다는 의미이다.
        fields = ['title', 'content',]
        # 모든 value를 가져오려면 all을 사용한다.
        # 단, 입력 가능한 형식만 받기 때문에
        # fields = '__all__'

        # 타이틀만 빼고 나머지를 출력하겠다는 의미이다.
        # exclude = ['title']
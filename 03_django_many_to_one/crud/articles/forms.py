from django import forms
from .models import Article, Comment


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude에 들어가 있는 내용은 알아서 넣어야 한다.
        # 위 아래 둘 중 아무거나 하자.
        # fields = '__all__'
        # exclude = ('article', )

        fields = ('content', )
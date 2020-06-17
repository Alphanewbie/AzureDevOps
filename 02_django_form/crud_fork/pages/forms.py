from django import forms
from .models import Pages

# 모델은 단수형으로
class PagesForm(forms.ModelForm):
    title = forms.CharField(
        # 원래는 maxlength가 존재하기 떼문에 알아서 막히지만, 위젯 선언하면 오버라이트 되서 그 옵션이 사라진다.
        max_length=20,
        widget=forms.TextInput(
            attrs={ 
                "class": "form-control",
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
    )
    class Meta:
        model = Pages
        fields = '__all__'

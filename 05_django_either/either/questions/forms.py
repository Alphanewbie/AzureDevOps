from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # 1개만 튜플로 만든거라 뒤에, 를 붙혀준다.
        exclude = ('user',)


class AnswerForm(forms.ModelForm):
    CHOICES = [
        ('a', 'RED'),
        ('b', 'BLUE'),
    ]

    choice = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Answer
        exclude = ('user', 'question',)
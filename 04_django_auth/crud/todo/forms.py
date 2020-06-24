from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    content= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    due_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class' : 'form-control'
            }
        )
    )

    class Meta:
        model = Todo
        fields = ('content', 'due_date')

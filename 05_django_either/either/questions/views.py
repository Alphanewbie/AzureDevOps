# get_object_or_404 오브젝트를 가져오거나 404를 보여주거나
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question

# Create your views here.
def index(request):
    return render(request,'questions/index.html')


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions:detail', question.pk)
        pass
    else:
        form = QuestionForm()
    context = {
        'form' : form
    }
    return render(request, 'questions/form.html', context)


def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    # pk를 조회해서 없다면 자동으로 404를 반환 아니면 위와 동일하게 작용한다.
    # 절대로 500을 찍히게 하면 안된다. - 500은 그냥 개발자 잘못.
    question = get_object_or_404(Question, pk=question_pk)
    answer_form = AnswerForm()
    context = {
        'question' : question,
        'answer_form' : answer_form,
    }
    return render(request, 'questions/detail.html', context)
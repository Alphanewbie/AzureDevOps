# get_object_or_404 오브젝트를 가져오거나 404를 보여주거나
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question

# Create your views here.
def index(request):
    return render(request, 'questions/index.html')


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'questions/form.html', context)


def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    # pk를 조회해서 없다면 자동으로 404를 반환 아니면 위와 동일하게 작용한다.
    # 절대로 500을 찍히게 하면 안된다. - 500은 그냥 개발자 잘못.
    question = get_object_or_404(Question, pk=question_pk)
    
    # 이 게시글에 달린 전체 답글을 가져온다.
    # 양방향 참조라서 자신을 참조한 것을 알아낼 수 있다.
    answers = question.answer_set.all()
    # 그 댓글에 필터를 걸어준다.
    # answer_a = answers.filter(choice='a')
    answer_a = answers.filter(choice='a').count()
    # answer_b = answers.filter(choice='b')
    answer_b = len(answers.filter(choice='b'))

    answer_form = AnswerForm()
    context = {
        'question': question,
        'answer_form': answer_form,
        'answer_a': answer_a,
        'answer_b': answer_b,
    }
    return render(request, 'questions/detail.html', context)


def answer_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
        return redirect('questions:detail', question_pk)
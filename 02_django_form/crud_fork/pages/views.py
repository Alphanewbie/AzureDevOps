from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Pages, Comment
from .forms import PagesForm, CommentForm


def index(request):
    pages = Pages.objects.all()

    context = {
        'pages' : pages,
    }
    return render(request, 'pages/index.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = PagesForm(request.POST)
        if form.is_valid():
            page=form.save()
            return redirect('pages:detail', page.pk)
    else:
        form = PagesForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/create.html', context)


def detail(request, pk):
    page = Pages.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'pages/detail.html', context)


@require_POST
def comment_create(request, pk):
    page = Pages.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.page = page
        comment.save()
    return redirect('pages:detail', page.pk)

@require_POST
def comment_delete(request, page_pk, comment_pk):
    page = Pages.objects.get(pk=page_pk)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('pages:detail', page.pk)
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Pages
from .forms import PagesForm

def index(request):
    return render(request,'pages/index.html')

@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = PagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = PagesForm()
    context = {
        'form' : form,
    }
    return render(request,'pages/create.html', context)
from django.shortcuts import render, redirect
from .models import Tasker
from .forms import TaskForm


def index(request):
    tasks = Tasker.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def cat_page(request):
    return render(request, 'main/cat_page.html')

def dog_page(request):
    return render(request, 'main/dog_page.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

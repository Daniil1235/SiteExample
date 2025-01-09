from django.shortcuts import render, redirect
from .models import Task, Priority
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "main/index.html", {"tasks": tasks})


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = 'При отправке формы произошла ошибка.'
    form = TaskForm()
    return render(request, "main/create.html", {"form": form, "error": error})
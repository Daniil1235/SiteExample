from django.shortcuts import render
from .models import Task, Priority
from .forms import TaskForm


def index(request):
    return render(request, "main/index.html")


def create(request):
    priorities = Priority.objects.all()
    form = TaskForm()
    return render(request, "main/create.html", {"priorities": priorities, "form": form})
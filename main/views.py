from django.shortcuts import render, redirect
from .models import Task, Priority
from .forms import TaskForm, NewUserForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib import messages


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "main/create.html"
    form_class = TaskForm
    extra_context = {"action": 'Обновление', "action_v": "Обновить"}


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "main/create.html"
    success_url = "/"
    extra_context = {"action": 'Удаление', "action_v": "Удалить"}


def index(request):
    sort = request.GET.get('sort')
    if not sort:
        sort = 'priority'
    tasks = Task.objects.all().order_by(sort)
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
    action = "Добавление"
    action_v = "Добавить"
    return render(request, "main/create.html", {"form": form, "error": error, "action": action, "action_v": action_v})


def detail_view(request, id):
    task = Task.objects.get(id=id)
    return render(request, "main/detail_view.html", {"task": task})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Успешная регистрация")
            return redirect("home")
        messages.error(request, "При регистрации произошла ошибка. Убедитесь, что данные введены верно")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})

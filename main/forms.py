from .models import Task
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'text', 'priority', 'deadline']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
            'priority': Select(attrs={'class': 'form-control', 'placeholder': 'Приоритет'}),
            'deadline': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
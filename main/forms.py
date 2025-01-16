from .models import Task
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, Select, RadioSelect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'text', 'priority', 'deadline']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Название'}),

            'description': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Краткое описание'}),

            'text': Textarea(attrs={'class': 'form-control',
                                    'placeholder': 'Текст'}),

            'priority': RadioSelect(attrs={'placeholder': 'Приоритет'}),

            'deadline': DateTimeInput(
                attrs={'class': 'form-control',
                       'type': 'datetime-local',
                       'style': 'width: 250px;'}),
        }



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
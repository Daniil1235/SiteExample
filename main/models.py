import django
from django.db import models


class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'приоритет'
        verbose_name_plural = 'приоритеты'


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Краткое описание', max_length=100)
    text = models.TextField('Текст заметки')
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, verbose_name='Приоритет')
    create_date = models.DateTimeField('Дата создания', default=django.utils.timezone.now, help_text="Не Трогай!!!")
    deadline = models.DateTimeField('Дедлайн (срок)')

    def get_absolute_url(self):
        return f"/tasks/{self.id}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
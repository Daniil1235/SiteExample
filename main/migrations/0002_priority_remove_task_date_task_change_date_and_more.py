# Generated by Django 5.1.4 on 2025-01-05 17:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='change_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Не Трогай!!!', verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Не Трогай!!!', verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дедлайн (срок)'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.priority', verbose_name='Приоритет'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-05 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'приоритет', 'verbose_name_plural': 'приоритеты'},
        ),
    ]

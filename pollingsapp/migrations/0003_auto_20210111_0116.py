# Generated by Django 3.1.5 on 2021-01-10 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollingsapp', '0002_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_question_id',
        ),
    ]

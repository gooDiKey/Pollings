from django.db import models

# Create your models here.

class Polling(models.Model):
    poll_title = models.CharField('Название опроса', max_length = 300)
    start_date = models.DateField('Дата старта опроса')
    end_date = models.DateField('Дата окончания опроса')
    poll_description = models.TextField('Описание опроса')

    def __str__(self):
        return self.poll_title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question_type_options = [
        ('text', 'Развернутый ответ'),
        ('one_opt', 'Выбор одного варианта ответа'),
        ('many_opt', 'Выбор нескольких вариантов ответа'),
    ]

    polling = models.ForeignKey(Polling, on_delete = models.CASCADE)
    question_text = models.CharField('Вопрос', max_length = 300)
    question_type = models.CharField('Тип вопроса', max_length = 50, choices = question_type_options, default = 'text')
    
    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    option_text = models.CharField('Ответ', max_length = 300)
    votes = models.IntegerField('Проголосовали', default = 0)
    
    def __str__(self):
        return self.option_text
    
    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    user = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


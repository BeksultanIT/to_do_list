from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Article(models.Model):
    title = models.CharField(max_length=75, verbose_name='Описание')
    status = models.CharField(max_length=20, choices=status_choices, default='new', verbose_name='Выборка')
    deadline = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)


    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'articles'

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Project(models.Model):

    date_start = models.DateField(verbose_name='Дата начала', )
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    name = models.CharField(max_length=75, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), related_name='projects', on_delete=models.SET_DEFAULT, default=1 ,verbose_name='Автор')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.id})



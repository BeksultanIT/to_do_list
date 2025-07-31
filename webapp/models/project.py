from django.db import models
from django.urls import reverse


class Project(models.Model):

    date_start = models.DateField(verbose_name='Дата начала', )
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    name = models.CharField(max_length=75, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('detail_task', kwargs={'pk': self.id})



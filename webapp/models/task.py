from django.db import models
from django.urls import reverse

from webapp.models.base_create_update import BaseCreateUpdateModel


class Task(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Описание')
    content = models.TextField(verbose_name='Контент', null=True, blank=True)
    deadline = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    status = models.ForeignKey("webapp.Statuses", related_name='task_status', on_delete=models.CASCADE, verbose_name='Статус', null=True, blank=True)
    types = models.ManyToManyField("webapp.Type", related_name='tasks', verbose_name='Тип', blank=True, through='webapp.TaskTypes', through_fields=('task', 'type'))
    project = models.ForeignKey("webapp.Project", related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


    def get_absolute_url(self):
        return reverse('detail_project', kwargs={'pk': self.project_id})
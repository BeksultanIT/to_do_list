
from django.db import models


class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления', null=True, blank=True)

    class Meta:
        abstract = True

class Task(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Описание')
    content = models.TextField(verbose_name='Контент', null=True, blank=True)
    deadline = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    status = models.ForeignKey("webapp.Statuses", related_name='task_status', on_delete=models.CASCADE, verbose_name='Статус', null=True, blank=True)
    types = models.ManyToManyField("webapp.Type", related_name='tasks', verbose_name='Тип', blank=True, through='webapp.TaskTypes', through_fields=('task', 'type'))


    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Statuses(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Статус')

    def __str__(self):
        return f"{self.id} - {self.title}"
    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Тип')

    def __str__(self):
        return f"{self.id} - {self.title}"
    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class TaskTypes(BaseCreateUpdateModel):
    task = models.ForeignKey('webapp.Task', related_name='task_types', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.Type', related_name='type_task', on_delete=models.CASCADE)


    class Meta:
        db_table = 'task_types'
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

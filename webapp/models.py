from datetime import timezone

from django.db import models

# Create your models here.
class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления', null=True, blank=True)

    class Meta:
        abstract = True

class Task(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Описание')
    content = models.TextField(verbose_name='Контент', null=True, blank=True)
    deadline = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    status = models.ForeignKey("webapp.Statuses", related_name='task_status', on_delete=models.CASCADE, verbose_name='Задача', null=True, blank=True)
    type = models.ForeignKey("webapp.Type", related_name='task_type', on_delete=models.CASCADE, verbose_name='Задача', null=True, blank=True)


    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'tasks'

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

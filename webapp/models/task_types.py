from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class TaskTypes(BaseCreateUpdateModel):
    task = models.ForeignKey('webapp.Task', related_name='task_types', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.Type', related_name='type_task', on_delete=models.CASCADE)


    class Meta:
        db_table = 'task_types'
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'
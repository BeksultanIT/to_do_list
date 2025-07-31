from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class Statuses(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Статус')

    def __str__(self):
        return f"{self.id} - {self.title}"
    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

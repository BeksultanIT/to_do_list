from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class Type(BaseCreateUpdateModel):
    title = models.CharField(max_length=75, verbose_name='Тип')

    def __str__(self):
        return f"{self.id} - {self.title}"
    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
from django.db import models


class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления', null=True, blank=True)

    class Meta:
        abstract = True
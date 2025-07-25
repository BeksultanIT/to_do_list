# Generated by Django 5.2.3 on 2025-07-11 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_statuses_created_at_alter_statuses_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_status', to='webapp.statuses', verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_type', to='webapp.type', verbose_name='Задача'),
        ),
    ]

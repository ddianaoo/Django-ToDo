# Generated by Django 4.2 on 2023-05-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_task_at_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='list',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='list',
            name='invite',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2 on 2023-05-16 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0013_alter_task_at_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='at_time',
            field=models.TimeField(default=datetime.time(21, 10, 22, 234775)),
        ),
    ]

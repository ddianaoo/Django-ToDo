# Generated by Django 4.2 on 2023-05-01 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_task_at_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='at_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 1, 18, 44, 30, 666677)),
        ),
    ]

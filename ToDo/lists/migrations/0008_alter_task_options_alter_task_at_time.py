# Generated by Django 4.2 on 2023-05-03 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_list_desc_alter_task_at_time_alter_task_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['at_time']},
        ),
        migrations.AlterField(
            model_name='task',
            name='at_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 3, 19, 31, 46, 757046)),
        ),
    ]

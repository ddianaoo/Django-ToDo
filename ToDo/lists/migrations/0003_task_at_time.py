# Generated by Django 4.2 on 2023-05-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_list_options_alter_task_options_task_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='at_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

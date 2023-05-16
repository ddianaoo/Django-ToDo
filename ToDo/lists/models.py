from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
import time


class List(models.Model):
    title = models.CharField(max_length=150, unique=True)
    desc = models.TextField(blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    invite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Task(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=False)
    is_done = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    at_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default=datetime.now().time())

    class Meta:
        ordering = ['at_time']

    def __str__(self):
        return f"Task name: {self.title} of {self.list}"
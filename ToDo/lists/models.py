from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    title = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Task(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=False)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Task name: {self.title} of {self.list}"
from rest_framework import serializers
from .models import Task, List


class ListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = List
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        fields['title'].initial = "My To Do List"
        return fields


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

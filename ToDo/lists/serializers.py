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


class CurrentListDefault:
    requires_context = True

    def __call__(self, serializer_field):
        list_id = serializer_field.context['request'].META['PATH_INFO'].split('/')[-3]
        my_list = List.objects.get(id=list_id)
        return my_list

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class TaskSerializer(serializers.ModelSerializer):
    list = serializers.HiddenField(default=CurrentListDefault())

    class Meta:
        model = Task
        fields = '__all__'

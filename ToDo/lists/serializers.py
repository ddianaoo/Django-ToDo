from rest_framework import serializers
from .models import Task, List
from django.shortcuts import render, redirect, get_object_or_404


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
        my_url = serializer_field.context['request'].META['PATH_INFO'].split('/')
        if len(my_url) == 6:
            list_id = my_url[-3]
        else:
            list_id = my_url[-4]
        my_list = get_object_or_404(List, id=list_id)
        return my_list

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class TaskSerializer(serializers.ModelSerializer):
    list = serializers.HiddenField(default=CurrentListDefault())

    class Meta:
        model = Task
        fields = '__all__'

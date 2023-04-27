from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='home'),
    path('lists/', login_required(get_lists), name='lists'),
    path('list/<int:id>/', login_required(get_tasks), name='tasks'),
    path('list/<int:list_id>/task/<int:task_id>/', login_required(task_details), name='task'),
    path('list/<int:list_id>/task/<int:task_id>/change/', login_required(change_task), name='change_task'),
    path('list/<int:list_id>/task/<int:task_id>/delete/', login_required(delete_task), name='delete_task'),
    path('list/<int:id>/add-task/', login_required(add_task), name='add_task'),
    path('list/create/', login_required(list_create), name='list_create'),
    path('list/<int:id>/delete/', login_required(list_delete), name='list_delete'),
]

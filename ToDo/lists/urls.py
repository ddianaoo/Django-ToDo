from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='home'),
    path('lists/', login_required(get_lists), name='lists'),
    path('list/<int:id>/', login_required(get_tasks), name='tasks'),
    path('list/create/', login_required(list_create), name='list_create'),
    path('list/<int:id>/delete/', login_required(list_delete), name='list_delete'),
]

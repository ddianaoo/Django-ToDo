from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('', get_lists, name='lists'),
    path('list/<int:id>/', get_tasks, name='tasks'),
    path('list/create/', list_create, name='list_create'),
    # path('list/create/', AddNews.as_view(), name='list_create'),
    path('list/<int:id>/delete/', list_delete, name='list_delete'),
]

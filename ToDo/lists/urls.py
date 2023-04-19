from django.urls import path
from .views import *


urlpatterns = [
    path('', get_lists, name='lists'),
    path('list/<int:id>/', get_tasks, name='tasks'),
]

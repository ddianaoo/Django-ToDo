from django.urls import path
from .views import *


urlpatterns = [
    path('lists/', get_lists, name='lists'),
]

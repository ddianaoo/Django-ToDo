from django.urls import path
from rest_framework import routers
from .views import ListViewSet, TaskViewSet


router = routers.SimpleRouter()
router.register(r'lists', ListViewSet, basename='List')
router.register(r'tasks', TaskViewSet, basename='Task')

urlpatterns = router.urls
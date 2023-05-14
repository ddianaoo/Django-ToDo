from django.urls import path,include
from rest_framework import routers
from .views import ListViewSet, TaskViewSet


router = routers.SimpleRouter()
router.register(r'', ListViewSet, basename='List')
#router.register(r'tasks', TaskViewSet, basename='Task')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:list_id>/tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
]
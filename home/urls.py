from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSets, basename='todo')

urlpatterns = [
    path('todo/', TodoView.as_view())
]

urlpatterns += router.urls
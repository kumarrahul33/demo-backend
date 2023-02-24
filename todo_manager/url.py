from django.urls import path
from todo_manager import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
]
from django.urls import path, include
from api_app.api.views import index, todo_list, todo_detail

urlpatterns = [
    path("", index, name="index"),
    path("todo/", todo_list, name="todo-list"),
    path("todo/<int:pk>/", todo_detail, name="todo-detail"),
]

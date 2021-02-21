from django.urls import path, re_path
from rest.views import TodoList, TodoDetail, CategoryList

urlpatterns = [
    path(r'todo/', TodoList.as_view()),
    path(r'category/', CategoryList.as_view()),
    re_path(r'todo/(?P<pk>[0-9]+)/', TodoDetail.as_view()),
]

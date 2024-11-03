from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('projects/<int:id>', views.project),
    path('tasks/', views.tasks),
    path('tasks/<int:id>', views.task),
    path('projects-view/', views.projectsHtml),
    path('tasks-view/', views.tasksHtml),
    path('tasks-view/<int:id>', views.tasksHtmlFromProject),
    path('create-task', views.createTask),
    path('create-project', views.createProject),
]

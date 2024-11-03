from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello,name='hello'),
    path('projects/', views.projects),
    path('projects/<int:id>', views.project),
    path('tasks/', views.tasks),
    path('tasks/<int:id>', views.task),
    path('projects-view/', views.projectsHtml, name='list-projects'),
    path('tasks-view/', views.tasksHtml, name='list-tasks'),
    path('tasks-view/<int:id>', views.tasksHtmlFromProject, name='list-tasks-project'),
    path('create-task', views.createTask, name='create-task'),
    path('create-project', views.createProject, name='create-project'),
]

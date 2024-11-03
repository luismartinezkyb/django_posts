from django.http import HttpResponse, JsonResponse
from myapp.models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from django.forms.models import model_to_dict
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
  title = 'Welcome to Django Course'
  
  return render(request, 'index.html', {
    'title': title,
  })
  return HttpResponse('Index page')
def hello(request, username):
  
  return HttpResponse('<h1>Hola %s</h1>' % username)
def about(request):
  return render(request, 'about.html')
  return HttpResponse('<h1>About</h1>')

def projectsHtml(request):
  projects = Project.objects.all()
  return render(request, 'projects/projects.html',{
    'projects': projects
  })
def tasksHtml(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks
  })
def tasksHtmlFromProject(request, id):
  tasks = Task.objects.filter(project_id=id)
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks
  })

def projects(request):
  projects = list(Project.objects.values())
  return JsonResponse(projects, safe=False)
  # return HttpResponse('<h1>Projects</h1>')
def project(request, id):
  result = Project.objects.get(id=id)
  return JsonResponse(result, safe=False)
  # return HttpResponse('<h1>Projects</h1>')
def tasks(request):
  p = Task.objects.all()
  return HttpResponse('<h1>tasks</h1>')
def task(request, id):
  # task = Task.objects.get(id=id)
  task = get_object_or_404(Task, id=id)
  result = model_to_dict(task)
  return JsonResponse(result, safe=False)
  return HttpResponse('<h1>Task: %s</h1>' %task.title)

def createTask(request):
  if(request.method == 'GET'):
    return render(request, 'tasks/create-task.html', {
      'form': CreateNewTask()
    })
  title = request.POST['title']
  description = request.POST['description']
  print(title)
  print(description)
  task = Task.objects.create(title=title, description=description, project_id=2)
  task.save()
  return redirect('list-tasks')

def createProject(request):
  if(request.method == 'GET'):
    return render(request, 'projects/create-project.html', {
      'form': CreateNewProject()
    })
  name = request.POST['name']

  project = Project.objects.create(name=name)
  project.save()
  return redirect('list-projects')

def projectDetail(request, id):
  project = get_object_or_404(Project, id=id);
  tasks = Task.objects.filter(project_id=project.id)
  return render(request, 'projects/project-detail.html', {
    'project': project,
    'tasks': tasks
  })
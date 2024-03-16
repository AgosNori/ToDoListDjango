
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render,redirect
from .form import CreateNewTask,CreateNewProject
# Create your views here.
def index(request):
    title = 'To do List with Django'
    return render (request, 'index.html',{
        'title':title,
    })

def hello(request,username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'Agostina'
    return render(request,'about.html',{
        'username':username,
    })

def projects(request):
    projects = list(Project.objects.values())
    return render(request,'project/projects.html',{
        'projects':projects
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    #tasks = list(Task.objects.values())
    tasks = Task.objects.all()
    return render(request,'task/tasks.html',{
        'tasks': tasks,
    })

def create_task(request):
    if request.method == 'GET':
        return render(request,'task/create_task.html',{
            'form': CreateNewTask()      
    })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=2)
        return redirect("/tasks/")
    

def create_project(request):
    if request.method == 'GET':
        return render(request,'project/create_project.html',{
            'form':CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        redirect('projects')

def project_detail(request,id):
    Project.objects.get(id=id)
    project= get_object_or_404(Project,id=id)
    task=Task.objects.filter(project_id=id)
    return render(request,'project/detail.html',{
        'project':'project',
        'tasks':task
    })
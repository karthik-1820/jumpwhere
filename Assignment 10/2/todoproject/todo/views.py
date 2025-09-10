from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')

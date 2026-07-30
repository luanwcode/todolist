from django.shortcuts import render, redirect
from django.http import HttpRequest
from . forms import TaskForm
from . models import TaskModel

def tasks_home(request):
    context = {
        "name": "Luan",
        "tasks": TaskModel.objects.all()
    }

    return render(request, 'tasks/home.html', context)

def tasks_add(request:HttpRequest):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")


    context = {
        "form": TaskForm
    }
    return render(request, 'tasks/add.html', context)

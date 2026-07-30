from django.shortcuts import render, redirect, get_object_or_404
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

def tasks_remove(request:HttpRequest, id):
    task = get_object_or_404(TaskModel, id=id)
    task.delete()

    return redirect("tasks:home")

def tasks_edit(request:HttpRequest, id):
    task = get_object_or_404(TaskModel, id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")

    form = TaskForm(instance=task)
    context = {
        "form": form
    }
    return render(request, 'tasks/edit.html', context)



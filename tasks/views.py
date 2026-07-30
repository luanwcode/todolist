from django.shortcuts import render
from django.http import HttpResponse

def tasks_home(request):
    context = {
        "name": "Luan"
    }

    return render(request, 'tasks/home.html', context)

def tasks_add(request):
    return HttpResponse("Here you can add your tasks")
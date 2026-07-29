from django.shortcuts import render
from django.http import HttpResponse

def tasks_home(request):
    return render(request, 'tasks/home.html')

def tasks_add(request):
    return HttpResponse("Here you can add your tasks")
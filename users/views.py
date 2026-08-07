from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def users_login(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("tasks:home")
        else:
            return HttpResponse('Invalid login credentials')

def users_register(request):
    if request.method == "GET":
        return render(request, "users/register.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('Username already registered')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('User sucessfully registered')
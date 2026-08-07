from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User

def users_login(request):
    return render(request, "users/login.html")

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
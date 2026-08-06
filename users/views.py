from django.shortcuts import render
from django.http import HttpRequest

def users_login(request):
    return render(request, "users/login.html")

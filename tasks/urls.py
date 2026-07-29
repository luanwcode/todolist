from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks_home),
    path("add", views.tasks_add)
]
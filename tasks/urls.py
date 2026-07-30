from django.urls import path
from . import views

app_name="tasks"

urlpatterns = [
    path("", views.tasks_home, name="home"),
    path("add", views.tasks_add, name="add")
]
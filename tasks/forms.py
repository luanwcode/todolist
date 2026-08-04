from django import forms
from . models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['name', 'description', 'completed', 'status']

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "bg-neutral-800 text-white border border-neutral-700 rounded-md px-3 py-2 w-full"
            }),
            "description": forms.Textarea(attrs={
                "class": "bg-neutral-800 text-white border border-neutral-700 rounded-md px-3 py-2 w-full"
            }),
        }

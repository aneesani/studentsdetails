from .models import Task
from django import forms

class Crudforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','age','place','course','date']
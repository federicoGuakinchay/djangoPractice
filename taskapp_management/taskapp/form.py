from django.forms import ModelForm
from django import forms
from .models import Task

class TaskUpdateForm(ModelForm):
  class Meta:
    model = Task
    fields = '__all__'
    exclude = ['completation_date','create_task']

class TaskCreateForm(ModelForm):
  limit_date = forms.DateField(
  widget=forms.DateInput(attrs={'type': 'date'}),)
  class Meta:
    model = Task
    fields = '__all__'
    exclude = ['completation_date','completed','create_task']

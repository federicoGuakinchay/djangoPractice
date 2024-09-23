from django.shortcuts import render,redirect,get_object_or_404
from .form import TaskCreateForm , TaskUpdateForm
from .models import Task
from django.utils import timezone

def task_list(request,order='importance',taskfilter='all'):
    tasks = filters_task(order,taskfilter)
    return render (request,'task_list.html',{'tasks':tasks,'order':order,'taskfilter':taskfilter})

def task_form(request):
  if request.method == 'GET':
    form = TaskCreateForm()
    return render (request,'task_form.html',{'form':form})
  elif request.method == 'POST':
    form = TaskCreateForm(request.POST)
    print (form.is_valid())
    if form.is_valid():
      form.save()
      return redirect('task_list')
    else:
      return render(request,'task_form.html',{'form':form})

def task_update(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  if request.method == 'GET':
    form = TaskUpdateForm(instance=task)
    return render(request,'task_form.html',{'form':form,'task_id':task_id})
  elif request.method == 'POST':
    form = TaskUpdateForm(request.POST, instance=task)
    if form.is_valid():
      if form.cleaned_data['completed']:
        if not task.completation_date :
          task.completation_date = timezone.now()
      else:
        task.completation_date = None
      form.save()
      return redirect('task_list')
    else:
      return render(request,'task_form.html',{'form':form,'task_id':task_id})
  print ('error')

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_complete(request,task_id):
  task = get_object_or_404(Task, id=task_id)
  task.completed = True
  task.completation_date = timezone.now()
  task.save()
  return redirect('task_list')

def task_incomplete(request,task_id):
  task = get_object_or_404(Task, id=task_id)
  task.completed = False
  task.completation_date = None
  task.save()
  return redirect('task_list')

def filters_task(order_filer,task_filter):
  if task_filter == 'incomplete':
    tasks_f1 = Task.objects.filter(completed=False)
  if task_filter == 'complete':
    tasks_f1 = Task.objects.filter(completed=True)
  if task_filter == 'all':
    tasks_f1 = Task.objects.all()
  if order_filer == 'importance':
    tasks_f2 = tasks_f1.order_by("-iportance_task__importance_value")
  if order_filer == 'limit_date':
    tasks_f2 = tasks_f1.order_by("limit_date")
  if order_filer == 'task_title':
    tasks_f2 = tasks_f1.order_by("title")
  return  tasks_f2
  
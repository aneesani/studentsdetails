
from .models import Task
from .forms import Crudforms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

def home(request):
  return render(request,'home.html')


def login(request):
    if request.method == 'POST':
      username = request.POST['username']
      password1 = request.POST['password1']
      user = auth.authenticate(username=username, password=password1)
      if user is not None:
        auth.login(request, user)
        return redirect('task_view')
      else:
        messages.info(request, 'invalid details')
        return redirect('login')
    else:
      return render(request, 'login.html')



def register(request):
  if request.method == 'POST':
      username = request.POST['username']
      password1 = request.POST['password1']
      email = request.POST['email']
      if password1 == password1:
        if User.objects.filter(username=username).exists():
          messages.info(request, "username taken")
          return redirect('register')
        elif User.objects.filter(email=email).exists():
          messages.info(request, "email taken")
          return redirect('register')
        else:
          user = User.objects.create_user(username=username, password=password1, email=email)
          user.save()
          print("user created")
      else:
        print("incorrect password")
        return redirect('register')
      return redirect('/')
  else:
   return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def task_view(request):
  tsk=Task.objects.all()
  if request.method=='POST':
    name=request.POST.get('name')
    age = request.POST.get('age')
    place = request.POST.get('place')
    course = request.POST.get('course')
    date = request.POST.get('date')
    ts=Task(name=name,age=age,place=place,course=course,date=date)
    ts.save()

  return render(request,'task_view.html',{'tsk':tsk})

def delete(request,taskid):
  task=Task.objects.get(id=taskid)
  if request.method=='POST':
    task.delete()
    return redirect('task_view')

  return render(request,'delete.html',{'task':task})


def update(request,id):
  task = Task.objects.get(id=id)
  form = Crudforms(request.POST or None,instance=task)
  if form.is_valid():
    form.save()
    return redirect('task_view')
  return render(request,'edit.html',{'task':task,'form':form})
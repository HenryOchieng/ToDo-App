from django.shortcuts import render, redirect

from .models import todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    task_items = todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'task_items' : task_items, 'form' : form}
    return render(request,'todolist/index.html',context)

@require_POST
def addToDoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_task = todolist(text=request.POST['text'])
        new_task.save()

    return redirect('index')

def completedTask(request, task_id):
    task = todolist.objects.get(pk=task_id)
    task.completed = True
    task.save()

    return redirect('index')

def deletecompleted(request):
    todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    todolist.objects.all().delete()

    return redirect('index')


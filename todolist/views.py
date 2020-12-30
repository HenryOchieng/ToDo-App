from django.shortcuts import render

from .models import todolist

# Create your views here.

def index(request):
    task_items = todolist.objects.order_by('id')
    context = {'task_items' : task_items}
    return render(request,'todolist/index.html',context)

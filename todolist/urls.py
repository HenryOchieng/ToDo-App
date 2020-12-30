from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addToDoItem, name='add'),
    path('completed/<task_id>', views.completedTask, name='completed'),
    path('deletecompleted', views.deletecompleted, name='deletecompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]
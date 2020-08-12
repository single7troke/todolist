from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('mylist/', views.mylist, name='Mylist'),
    path('mylist/add/', views.add, name='add'),
    path('mylist/done/<int:todo_id>/', views.done, name='done'),
    path('mylist/delete/<int:todo_id>/', views.delete, name='delete'),

]

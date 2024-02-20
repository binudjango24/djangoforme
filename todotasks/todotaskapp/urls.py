from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.addtask,name='addtask'),
    path('details/',views.details,name='details'),
    path('delete/<int:taskId>/',views.delete,name='delete'),
    path('update/<int:taskId>/', views.update, name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
     path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]

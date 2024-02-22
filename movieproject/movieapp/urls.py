from django.contrib import admin
from django.urls import path,include
from . import  views
app_name = 'movieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movieId>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.updatemovie,name ='updatemovie'),
    path('delete/<int:id>/',views.delete,name ='delete')

    # path('movie/<int:movieId>/', views.urlpage, name='urlpage')
]

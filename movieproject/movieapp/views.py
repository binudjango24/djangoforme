from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import movie
from  . forms import  movieform

# Create your views here.

def index(request):
    movies=movie.objects.all()
    context={'movies_list':movies}
    return render(request,'index.html',context)
def detail(request,movieId):
    mmovie=movie.objects.get(id=movieId)
    return render(request,"detail.html",{'movielist':mmovie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        imge = request.FILES['image']
        movielist=movie(name=name,desc=desc,year=year,img=imge)
        movielist.save()
    return render(request,"add.html")
def updatemovie(request,id):
    movies=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':movies})
def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')



# def urlpage(request,movieId):
#     mmovie=movie.objects.get(id=movieId)
#     return render(request,"detail.html",{'movielist':mmovie})


from django.shortcuts import render
from .models import Place, managment


# Create your views here.
def mainpage(request):
    obj=Place.objects.all()
    manager=managment.objects.all()
    return render(request,"index.html",{'result':obj,'execdir':  manager})
# def about(request):
#     return render(request,"about.html",{})

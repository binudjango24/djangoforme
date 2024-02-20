from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Todotask
from .forms import TodoForm
from   django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class TaskListView(ListView):
    model=Todotask
    template_name = 'homepage.html'
    context_object_name = 'getTask'
class TaskDetailView(DetailView):
        model = Todotask
        template_name = 'detail.html'
        context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model=Todotask
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Todotask
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def addtask(request):
    getTask = Todotask.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        task = Todotask(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'homepage.html',{'getTask':getTask})
def details(request):
    task=Todotask.objects.all()
    return render(request,'detail.html',{'task':task})
def delete(request,taskId):
    getTask=Todotask.objects.get(id=taskId)
    if request.method=='POST':
        getTask.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,taskId):
    getTask=Todotask.objects.get(id=taskId)
    form=TodoForm(request.POST or None,instance=getTask)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'getTask':getTask})



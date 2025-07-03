from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task, status_choices


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.htm', {'tasks': tasks})

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        content = request.POST.get('content')
        article = Task.objects.create(title=title, status=status, deadline=deadline, content=content)
        return redirect('detail_task', pk=article.id)
    else:
        return render(request, 'new.html', {'status_choices': status_choices})

def update_task(request, *args,pk, **kwargs ):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.content = request.POST.get('content')
        task.save()
        return redirect('detail_task', pk=task.pk)
    else:
        return render(request, 'update_task.html', {'task': task,  'status_choices':status_choices}, )

def delete_task(request, *args,pk, **kwargs ):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        return render(request, 'delete_task.html', {'task': task,  'status_choices':status_choices}, )

def detail_article(request,*args,pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_article.html', {'task': task})

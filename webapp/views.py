from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm, BulkDeleteForm
from webapp.models import Task, status_choices



def index(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('selected_tasks')
        if task_ids:
            Task.objects.filter(id__in=task_ids).delete()
        return redirect('index')

    tasks = Task.objects.order_by('-id')
    bulk_form = BulkDeleteForm()
    return render(request, 'index.html', {'tasks': tasks, 'bulk_form': bulk_form})


def new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            status = form.cleaned_data.get('status')
            deadline = form.cleaned_data.get('deadline')
            content = form.cleaned_data.get('content')
            task = Task.objects.create(title=title, status=status, deadline=deadline, content=content)
            return redirect('detail_task', pk=task.pk)
        else:
            return redirect(request,'add_task', {"form":form} )
    else:
        form = TaskForm()
        return render(request, 'new.html', {'status_choices': status_choices, 'form': form})

def update_task(request, *args,pk, **kwargs ):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.status = form.cleaned_data.get('status')
            task.deadline = form.cleaned_data.get('deadline')
            task.content = form.cleaned_data.get('content')
            task.save()
            return redirect('detail_task', pk=task.pk)
        else:
            return redirect(request,'update_task', {"form":form} )
    else:
        form = TaskForm(initial={
            'title': task.title,
            'status': task.status,
            'deadline': task.deadline,
            'content': task.content,
        })
        return render(request, 'update_task.html', {'form': form,  'status_choices':status_choices}, )

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

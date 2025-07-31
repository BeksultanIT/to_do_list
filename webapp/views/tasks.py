from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm, BulkDeleteForm
from webapp.models import Task


class TaskListView(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('-id')
        context['bulk_form'] = BulkDeleteForm()
        return context

    def post(self, request, *args, **kwargs):
        task_ids = request.POST.getlist('selected_tasks')
        if task_ids:
            Task.objects.filter(id__in=task_ids).delete()
        return redirect('index')


class CreateTaskView(TemplateView):
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            deadline = form.cleaned_data.get('deadline')
            content = form.cleaned_data.get('content')
            status = form.cleaned_data.get('status')
            types = form.cleaned_data.get('types')
            task = Task.objects.create(title=title, deadline=deadline, content=content, status=status)
            task.types.set(types)
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'tasks/new.html', {"form":form})
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/new.html', {'form': form})

class UpdateTaskView(View):
    def post(self, request, *args,pk, **kwargs ):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.deadline = form.cleaned_data.get('deadline')
            task.content = form.cleaned_data.get('content')
            task.status = form.cleaned_data.get('status')
            task.save()
            task.types.set(form.cleaned_data.get('types'))
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'tasks/update_task.html', {"form":form})
    def get(self, request, *args,pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
                'title': task.title,
                'deadline': task.deadline,
                'content': task.content,
                'status': task.status,
                'types': task.types.all(),
            })
        return render(request, 'tasks/update_task.html', {'form': form}, )

class DeleteTaskView(View):
    def get(self, request, *args,pk, **kwargs ):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'tasks/delete_task.html', {'task': task}, )

    def post(self, request, *args,pk, **kwargs ):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')



class DetailTaskView(TemplateView):
    template_name = 'tasks/detail_article.html'

    def get_context_data(self, **kwargs):
        context = super(DetailTaskView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        return context


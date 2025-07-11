from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView

from webapp.forms import TaskForm, BulkDeleteForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

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
            return render(request,'new.html', {"form":form} )
    def get(self, request):
        form = TaskForm()
        return render(request, 'new.html', { 'form': form})

class UpdateView(View):
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
            return render(request,'update_task.html', {"form":form} )
    def get(self, request, *args,pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
                'title': task.title,
                'deadline': task.deadline,
                'content': task.content,
                'status': task.status,
                'types': task.types.all(),
            })
        return render(request, 'update_task.html', {'form': form}, )

class DeleteView(View):
    def get(self, request, *args,pk, **kwargs ):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'delete_task.html', {'task': task}, )

    def post(self, request, *args,pk, **kwargs ):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')



class DetailView(TemplateView):
    template_name = 'detail_article.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        return context


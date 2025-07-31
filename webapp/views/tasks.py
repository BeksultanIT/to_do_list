from urllib.parse import urlencode

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView

from webapp.forms import TaskForm, BulkDeleteForm, SearchForm
from webapp.models import Task, Project


class TaskListView(ListView):
    template_name = 'projects/index.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result["query"] = urlencode({"search": self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


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


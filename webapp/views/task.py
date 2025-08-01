from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import TaskForm
from webapp.models import Project, Task


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "tasks/new_task.html"
    form_class = TaskForm


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
     model = Task
     form_class = TaskForm
     template_name = "tasks/update_task.html"



class DeleteTaskView( LoginRequiredMixin, DeleteView):
    model = Task


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)


    def get_success_url(self):
        return self.object.get_absolute_url()




class DetailTaskView(DetailView):
    template_name = 'tasks/detail_task.html'
    model = Task
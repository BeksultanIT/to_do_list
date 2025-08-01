from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Project, Task


class CreateTaskView(CreateView):
    template_name = "tasks/new_task.html"
    form_class = TaskForm


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('detail_project', kwargs={'pk': self.object.project_id})

class UpdateTaskView(UpdateView):
     model = Task
     form_class = TaskForm
     template_name = "tasks/update_task.html"

     # def success_url(self):
     #     return reverse('detail_project', kwargs={'pk': self.object.project.pk})


class DeleteTaskView(DeleteView):
    model = Task


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)


    def get_success_url(self):
        return self.object.get_absolute_url()


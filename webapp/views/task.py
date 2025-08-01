from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import TaskForm
from webapp.models import Project


class CreateTaskView(CreateView):
    template_name = "tasks/new_task.html"
    form_class = TaskForm


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('detail_project', kwargs={'pk': self.object.project_id})


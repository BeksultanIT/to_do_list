from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, ProjectForm
from webapp.models import  Project


class ProjectListView(ListView):
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


class CreateProjectView(CreateView):
    template_name = "projects/new.html"
    form_class = ProjectForm


class UpdateProjectView(UpdateView):
    template_name = "projects/update_project.html"
    form_class = ProjectForm
    model = Project


class DeleteProjectView(DeleteView):
    model = Project
    template_name = "projects/delete_project.html"
    success_url = reverse_lazy('index')




class DetailProjectView(DetailView):
    template_name = 'projects/detail_project.html'
    model = Project

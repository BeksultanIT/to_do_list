from django import forms
from django.forms import widgets, DateInput

from webapp.models import Task, Type, Statuses


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Title', widget=widgets.Input(attrs={'class': 'form-control'}))
    content = forms.CharField( required=True, label='Content', widget=forms.Textarea(attrs={'class': 'form-control'}))
    deadline = forms.DateField(required=True, label='Deadline',  widget=forms.DateInput(attrs={'type': 'date'}))
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Type', widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(queryset=Statuses.objects.all(), required=True, label='Status', widget=forms.Select(attrs={'class': 'form-control'}))


class BulkDeleteForm(forms.Form):
    selected_tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
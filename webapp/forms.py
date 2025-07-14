from django import forms
from django.forms import widgets

from webapp.models import Task, Type, Statuses



class TaskForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs['class'] = 'form-control'


    deadline = forms.DateField(
        required=True,
        label='Deadline',
        widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline','status', 'types',]
        widgets = {
            'types': forms.CheckboxSelectMultiple(),
        }


class BulkDeleteForm(forms.Form):
    selected_tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
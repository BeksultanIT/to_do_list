from django import forms
from django.core.exceptions import ValidationError
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



    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long")
        return title

    def clean(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if title and content and title == content:
            raise ValidationError("Название и контент не могут быть одинаковыми")
        return self.cleaned_data


class BulkDeleteForm(forms.Form):
    selected_tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
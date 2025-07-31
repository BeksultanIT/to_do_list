from django import forms


from webapp.models import  Project



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'date_start', 'date_end']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_end': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
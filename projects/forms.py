from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags'] 

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),   
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name == 'description':
                field.widget.attrs.update({'class': 'input', 'placeholder': 'Add description'})
            elif name == 'demo_link':
                field.widget.attrs.update({'class': 'input', 'placeholder': 'Add demo link'})
            elif name == 'source_link':
                field.widget.attrs.update({'class': 'input', 'placeholder': 'Add source link'})
            elif name == 'tags':
                field.widget.attrs.update({'class': 'input', 'placeholder': 'Add tags'})

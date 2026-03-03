from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'rows':5, 'cols':20}),

        }
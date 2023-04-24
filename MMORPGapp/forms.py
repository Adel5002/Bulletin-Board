
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'categories', 'upload')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'upload': forms.FileInput(attrs={'class': 'form-control'}),
        }


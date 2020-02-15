from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        # All Conent -> fields = '__all__'
        fields = ['title', 'body']
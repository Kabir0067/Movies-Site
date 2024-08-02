from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'description', 'video_file', 'image', 'category', 'channel_name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

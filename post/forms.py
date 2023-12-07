from django import forms
from . models import Post
 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
            'category': 'Post Categories',
            'author': 'Select Author'
        }
        widgets = {
            'category': forms.CheckboxSelectMultiple()
        }

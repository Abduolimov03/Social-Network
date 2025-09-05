from django import forms
from .models import Post, Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a comment...',
                'class': 'form-control'
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'media']
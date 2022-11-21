from .models import Comment, Post
from django.db import models
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
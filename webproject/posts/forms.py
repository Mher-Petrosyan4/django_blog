from django import forms
from django.core.exceptions import ValidationError

from posts.models import Post


class PostsModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =['image', 'caption', 'no_of_likes']
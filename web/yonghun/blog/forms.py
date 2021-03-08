# from importlib._common import _


from django import forms

from ..models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        fields = {'type', 'title', 'content'}
        model = Blog
        labels = {
            "type": "구분",
            "title": '제목',
            "content": "내용",
        }


class BlogCommentForm(forms.ModelForm):
    class Meta:
        fields = {
            'parent',
            'comment'
        }
        labels = {
            "comment": "내용",
        }
        widgets = {
            'parent': forms.HiddenInput
        }

        model = BlogComment

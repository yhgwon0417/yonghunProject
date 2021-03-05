# from importlib._common import _


from django import forms

from ..models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Blog
        labels = {
            "title": '제목',
            "content": "내용",
        }


class BlogCommentForm(forms.ModelForm):
    class Meta:
        fields = {
            'user', 'comment'
        }
        model = BlogComment

        labels = {
            "comment": "내용",
        }
        # widgets = {
        #     'parent': forms.HiddenInput(),
        # }

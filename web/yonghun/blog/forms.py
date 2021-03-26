# from importlib._common import _


from django import forms

from ..models import Blog, Comment


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
        model = Comment
        fields = [
            'id',
            'blog',
            'created_by',
            'parent',
            'comment',
        ]
        widgets = {
            # 'id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'blog': forms.TextInput(attrs={'readonly': 'readonly'}),
            'parent': forms.TextInput(attrs={'readonly': 'readonly'}),
            'created_by': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

        labels = {
            "comment": "내용",
        }

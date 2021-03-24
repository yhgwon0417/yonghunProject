# from importlib._common import _


from django import forms

from ..models import Blog, BlogComment




class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
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

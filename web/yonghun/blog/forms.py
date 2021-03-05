# from importlib._common import _


from django import forms


from ..models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Blog
        labels = {
            "title": '제목',
            "content": "내용",
        }

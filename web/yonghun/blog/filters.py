from django_filters import FilterSet, ChoiceFilter, CharFilter, ModelChoiceFilter

from ..models import Blog, BlogType


class Blogfilter(FilterSet):
    type = ModelChoiceFilter(field_name='type__name',  label="구분", queryset=BlogType.objects.all())
    title = CharFilter(lookup_expr='icontains', label="제목")
    content = CharFilter(lookup_expr='icontains', label="내용")

    class Meta:
        model = Blog

        fields = ['title' ]

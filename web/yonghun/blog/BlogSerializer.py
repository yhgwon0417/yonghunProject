from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    # pagination_class = PageNumberPagination
    serializer_class = BlogSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type', 'title')

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

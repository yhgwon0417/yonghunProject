
from rest_framework import serializers, viewsets

from ..models import Comment, BlogType


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = '__all__'


class TypeViewSet(viewsets.ModelViewSet):
    queryset = BlogType.objects.all()

    serializer_class = TypeSerializer

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('name',)


from rest_framework import serializers, viewsets

from ..models import BlogType


class TypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    class Meta:
        model = BlogType
        fields = '__all__'


class TypeViewSet(viewsets.ModelViewSet):
    queryset = BlogType.objects.all()

    serializer_class = TypeSerializer

    

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('name',)

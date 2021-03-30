from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets

from ..models import Schedule, Inspection, System


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()

    serializer_class = SystemSerializer

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

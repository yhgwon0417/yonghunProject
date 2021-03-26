from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets

from ..models import Schedule, Inspection


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()

    serializer_class = InspectionSerializer

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

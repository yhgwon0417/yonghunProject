from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets

from ..models import Schedule, Inspection, System


class InspectionSerializer(serializers.ModelSerializer):
    system = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Inspection
        fields = '__all__'




class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()

    serializer_class = InspectionSerializer

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

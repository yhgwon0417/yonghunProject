from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..inspection.InspectionSerializer import InspectionSerializer
from ..models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    inspection_set = InspectionSerializer(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()

    serializer_class = ScheduleSerializer

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

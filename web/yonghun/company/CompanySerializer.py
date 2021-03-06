from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Company
from ..schedule.ScheduleSerializer import ScheduleSerializer


class CompanySerializer(serializers.ModelSerializer):
    schedule_set = ScheduleSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, SAFE_METHODS
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import Company
from ..schedule.ScheduleSerializer import ScheduleSerializer


class IsAdminUserOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class CompanySerializer(serializers.ModelSerializer):
    schedule_set = ScheduleSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_schedule_set(self, instance):
        schedules = instance.schedule_set.all().order_by('start_date')
        return ScheduleSerializer(schedules, many=True).data


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = [IsAdminUserOrManager]

    filter_backends = (DjangoFilterBackend,)

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

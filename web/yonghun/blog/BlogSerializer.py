from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import Blog, BlogType

from ..type import TypeSerializer


class BlogSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    type = TypeSerializer.TypeSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, viewsets

from ..models import Blog

from ..type import TypeSerializer


class BlogSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname')
    type = TypeSerializer.TypeSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('type', 'title')
    #
    # filter_fields = '__all__'
    # ordering_fields = '__all__'
    # search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

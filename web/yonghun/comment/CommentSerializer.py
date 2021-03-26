from rest_framework import serializers, viewsets

from ..models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)

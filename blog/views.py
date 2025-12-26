from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], url_path='myposts')
    def myposts(self, request):
        posts = Post.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='latest')
    def latest(self, request):
        posts = Post.objects.order_by('-publish_date')[:5]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='featured')
    def featured(self, request):
        posts = Post.objects.filter(featured=True)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

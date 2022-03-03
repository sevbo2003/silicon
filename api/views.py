from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

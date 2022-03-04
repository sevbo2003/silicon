from rest_framework import generics
from blog.models import Post
from accounts.models import CustomUser
from .serializers import PostSerializer, UserSerializer


class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

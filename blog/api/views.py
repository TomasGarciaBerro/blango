from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostList(generics.ListCreateAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
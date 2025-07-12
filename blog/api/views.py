from rest_framework import generics
from blog.permissions import AuthorModifyOrReadOnly
from blog.api.serializers import PostSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)

from rest_framework import generics
from vollclub.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, SAFE_METHODS

class PostUserWritePermission(BasePermission):
    message = 'Редактировать посты могут только авторы.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: 
            return True 

        return obj.author == request.user 

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


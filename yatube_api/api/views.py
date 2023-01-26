from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from posts.models import Group, Post
from .serializers import (CommentSerializer,
                          GroupSerializer, PostSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
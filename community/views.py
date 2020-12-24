from rest_framework import viewsets

from .models import Comment, Post
from .permissions import IsAuthor
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(active=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthor]

    def retrieve(self, request, *args, **kwargs):
        # Increase a number of views.
        post = Post.objects.get(pk=self.kwargs['pk'])
        post.views += 1
        post.save()
        return super().retrieve(self, request, *args, **kwargs)


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            author=self.kwargs['author_pk'], active=True)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Comment.objects.filter(
            post=self.kwargs['post_pk'], parent=None)

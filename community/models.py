from django.db import models

from users.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_posts')
    active = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.TextField()
    content = models.TextField()
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published']


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='children')
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['rating', '-published']

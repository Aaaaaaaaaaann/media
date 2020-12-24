from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    comments_number = serializers.SerializerMethodField('count_numbers')

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'author_name',
            'published',
            'updated',
            'title',
            'content',
            'rating',
            'views',
            'comments_number',
        ]

    def count_numbers(self, instance):
        return Comment.objects.filter(post=instance).count()

    def create(self, validated_data):
        """Check if user's IDs in a request coincide."""
        if validated_data['author'].pk != self.context['request'].user.pk:
            raise serializers.ValidationError('Wrong user ID.')
        new_post = Post.objects.create(**validated_data)
        return new_post


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    children = serializers.SerializerMethodField('get_children')

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'author_name',
            'parent',
            'content',
            'published',
            'updated',
            'rating',
            'children',
        ]

    def get_children(self, instance):
        children = Comment.objects.filter(parent=instance)
        serializer = CommentSerializer(children, many=True)
        return serializer.data

    def create(self, validated_data):
        """Check if user's IDs in a request coincide."""
        if validated_data['author'].pk != self.context['request'].user.pk:
            raise serializers.ValidationError('Wrong user ID.')
        new_comment = Comment.objects.create(**validated_data)
        return new_comment

from rest_framework import serializers
from forum.models import Thread, Post
from django.contrib.auth.models import User

class ThreadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Thread
        fields = ('id', 'subject',)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'created_date', 
            'last_edited_date', 'thread',)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
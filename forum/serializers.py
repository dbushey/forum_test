from rest_framework import serializers
from forum.models import Thread, Post
#from django.contrib.auth.models import User

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('subject',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'class', 'created_date', 
            'last_edited_date', 'thread')
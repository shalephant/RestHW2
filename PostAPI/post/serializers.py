from django.contrib.auth.models import User
from rest_framework import serializers

from PostAPI.post.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email"
        ]




class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "user",
            "slug"
        ]
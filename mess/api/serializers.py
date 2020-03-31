from rest_framework import serializers
from mess.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['is_anonymous','author','text']

from rest_framework import serializers
from mess.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['is_anonymous','author','text']

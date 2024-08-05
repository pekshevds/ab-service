from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    token = serializers.UUIDField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()

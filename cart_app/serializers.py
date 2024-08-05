from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()


class CartSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
    qnt = serializers.DecimalField(max_digits=15, decimal_places=3)

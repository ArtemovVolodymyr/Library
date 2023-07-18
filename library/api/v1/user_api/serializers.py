from rest_framework import serializers
from authentication.models import CustomUser
from order.models import Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'role')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'book', 'user', 'created_at', 'end_at', 'plated_end_at')
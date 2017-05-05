from rest_framework import serializers
from .models import Bucketlist

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Customer
    fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class MenuSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Menu
    fields = ('id', 'category')

class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Menu
    fields = ('id', 'name', 'menu')

class OrderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Menu
    fields = ('id', 'order_items')

class FoodItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Menu
    fields = ('id', 'name', 'price')

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

  class Meta:
      """Meta class to map serializer's fields with the model fields."""
    model = Menu
    fields = ('id', 'item', 'quantity')

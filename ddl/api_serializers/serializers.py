from rest_framework import serializers
from ddl import models
from ddl.models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
      model = Consumer
      fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class MenuSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = Menu
      fields = ('id', 'category')

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Restaurant
        fields = ('id', 'name', 'menu')

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'order_items')

class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FoodItem
        fields = ('id', 'name', 'price')

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FoodItem
        fields = ('id', 'quantity')

class OrderCartSerializer(serializers.ModelSerializer):
    order_items = serializers.ListField()
    class Meta:
        model = OrderCart
        fields = ('id', 'order_items')

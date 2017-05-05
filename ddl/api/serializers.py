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
	order_items = serializers.ListField(
   order=OrderItemSerializer,
	)

  class Meta:
    model = OrderCart
    fields = ('id', 'order_items')

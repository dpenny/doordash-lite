from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from api_serializers.serializers import CustomerSerializer, FoodItemSerializer
from rest_framework import mixins, viewsets
from django.http import Http404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Consumer, FoodItem, OrderCart

class CustomerDetailView(DetailView):
  model = Consumer
  def get(self, request, consumer_id, *args, **kwargs):
    customer = None
    try: 
      customer = Consumer.objects.get(id=consumer_id)
    except ObjectDoesNotExist:
      raise Http404 
    return HttpResponse('Hello, World!')


class CustomerListView(mixins.ListModelMixin):
  model = Consumer

  # Get all the customers in the database
  def list(self, request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

class FoodItemListView(mixins.ListModelMixin):
  model = FoodItem

  # Get all the food items available
  def list(self, request):
    food_items = FoodItem.objects.filter(available=True)
    serializer = FoodItemSerializer(food_items, many=True)
    return Response(serializer.data)

class OrderCartListView(mixins.ListModelMixin):
  model = OrderCart

  # Get all the OCs in database
  def list(self, request):
    order_carts = OrderCart.objects.filter(available=True)
    serializer = OrderCartSerializer(food_items, many=True)
    return Response(serializer.data)


class OrderCartDetailView(DetailView):
  # Get the information for one specific order cart
  def get(self, request, order_cart_id, *args, **kwargs):
    oc = OrderCart.objects.get(id=order_cart_id)
    serializer = OrderCartSerializer(customer)
    return Response(serializer.data)

  def add_order_item_to_cart(self, order_cart_id, item_id_list):
    oc = OrderCart.objects.get(id=order_cart_id)
    oc.order_items.append(order_item_list)
    oc.save()



from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from api.serializers import CustomerSerializer, FoodItemSerializer
from rest_framework import mixins, viewsets
from django.http import Http404

from models import Customer, FoodItem, OrderCart

class CustomerDetailView(DetailView, viewsets.ViewSet):
  def get(self, request, customer_id, *args, **kwargs):
    customer = None
    try: 
      customer = Customer.objects.get(id=customer_id)
    except ObjectDoesNotExist:
      raise Http404 
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)


class CustomerListView(mixins.ListModelMixin):
  model = Customer

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


class OrderCartDetailView(DetailView, viewsets.ViewSetQ):
  # Get the information for one specific order cart
  def get(self, request, order_cart_id, *args, **kwargs):
    oc = OrderCart.objects.get(id=order_cart_id)
    serializer = OrderCartSerializer(customer)
    return Response(serializer.data)

  # Check out an order cart
  # is this the best place to put the function?
  def checkout_order_cart(self, order_cart_id, request,  *args, **kwargs):
     oc = OrderCart.objects.get(id=order_cart_id)
     oc.has_checked_out = True
     oc.save()
     # do other checkout logic here
    return True



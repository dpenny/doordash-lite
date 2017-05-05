from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from api.serializers import CustomerSerializer, FoodItemSerializer

from models import Customer, FoodItem

class CustomerDetailView(DetailView):
  def get(self, request, customer_id, *args, **kwargs):
    customer = Customer.objects.get(id=customer_id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)


class CustomerListView(ListView):
  model = Customer

  # Get all the customers in the database
  # could modify this to return either list with filter or all if no filters are specified
  def get(self, request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


class FoodItemListView(ListView):
  model = FoodItem

  # Get all the food items available
  # could modify this to return either list with filter or all if no filters are specified
  def get(self, request):
    food_items = FoodItem.objects.filter(available=True)
    serializer = FoodItemSerializer(food_items, many=True)
    return Response(serializer.data)

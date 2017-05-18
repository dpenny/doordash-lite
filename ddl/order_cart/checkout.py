from models import OrderCart
from rest_framework.response import Response
from api.serializers import OrderCartSerializer

def checkout_order_cart(order_cart, request,  *args, **kwargs):
   order_cart.has_checked_out = True
   oc.save()
   serializer = OrderCartSerializer(order_cart)
   # do other checkout logic here
  return Response(serializer.data)
from django.views.generic.detail import DetailView
from api.serializers import CustomerSerializer
from models import Customer

class CustomerDetailView(DetailView):
  def get(self, request, customer_id, *args, **kwargs):
    customer = Customer.objects.get(id=customer_id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)
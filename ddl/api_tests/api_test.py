from .api import CustomerDetailView
from rest_framework.test import APITestCase

class TestAPI(APITestCase):
    def setup(self):
        self.view = CustomerDetailView()
        
        
    def test_get(self):
        pass

from ddl.models import FoodItem, Consumer
from django.test import TestCase
import unittest
from django.test import Client
import pytest
pytestmark = pytest.mark.usefixtures("initdb")
from django.test.client import RequestFactory
from rest_framework.test import APITestCase


class TestStuff(unittest.TestCase):
  @pytest.fixture(autouse=True, scope='session')
  def setUp(self):
    self.client = Client()
    Consumer.objects.create(first_name="foo", last_name="foo", email="foofoo", phone_number="foo")
    self.factory = RequestFactory()

  @pytest.fixture(autouse=True, scope='session')
  def test_get_existing_customer(self):
    response = self.client.get('/ddl/customers/1/')
    self.assertEqual(response.status_code, 200)

  @pytest.fixture(autouse=True, scope='session')
  def test_get_nonexisting_customer(self):
    response = self.client.get('/ddl/customers/100/')
    self.assertEqual(response.status_code, 404)

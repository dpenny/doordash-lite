# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from .models import FoodItem
import django
django.setup()

def test_unicode():
  apple = FoodItem(name='apple')
  assert apple.name == 'apple'
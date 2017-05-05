# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Menu(models.Model):
  class Meta:
    db_table = 'menu'

  category = models.TextField()

class FoodItem(models.Model):
  class Meta:
    db_table = 'food_item'
  name = models.TextField()
  price = models.IntegerField()
  available = models.BooleanField()

class OrderItem(models.Model):
  class Meta:
    db_table = 'order_item'

  item = models.ForeignKey(FoodItem, blank=True)
  quantity = models.IntegerField()

class Customer(models.Model):
  class Meta:
    db_table = 'customer'
  first_name = models.TextField()
  last_name = models.TextField()
  email = models.TextField()
  phone_number = models.IntegerField()

  #Create a new customer in the database
  @classmethod
  def create(cls, first_name, last_name, email, phone_number):
    customer = cls(first_name=first_name, last_name= last_name,
      email=email, phone_number=phone_number)
    customer.save()
    return customer

class Restaurant(models.Model):
  class Meta:
    db_table = 'restaurant'

  name = models.TextField()
  menu = models.ForeignKey(Menu, blank=True)

class OrderCart(models.Model):
  class Meta:
    db_table = 'order_cart'

  order_items = models.ManyToManyField(OrderItem, blank=True)

class Order(models.Model):
  class Meta:
    db_table = 'order_table'

  customer = models.ForeignKey(Customer)
  order_cart = models.ForeignKey(OrderCart)
  #add delivery once added to table




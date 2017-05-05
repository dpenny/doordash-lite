# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Address(models.Model):
  class Meta:
    db_table = 'address_table'
  address = models.TextField()
  city = models.TextField()
  state = models.TextField()


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

# Get all the customers in the database
class Customer(models.Model):
  class Meta:
    db_table = 'customer'
  first_name = models.TextField()
  last_name = models.TextField()
  email = models.TextField()
  phone_number = models.IntegerField()
  def get(self, request):
    return self.objects.all()

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

  #Get all the order carts in the database
  # could modify this to return either list with filter or all if no filters are specified
  def get(self, request):
    return self.objects.all()

  #Add food items to the order cart
  #  sketch???
  def update(self, order_item_list):
    self.order_items.append(order_item_list)
    self.save()

  #Create a new ordercart
  @classmethod
  def create(cls, order_items):
    order_cart = cls(order_items=order_items)
    order_cart.save()
    return order_cart

class Order(models.Model):
  class Meta:
    db_table = 'order_table'

  customer = models.ForeignKey(Customer)
  order_cart = models.ForeignKey(OrderCart)
  address = models.ForeignKey(Address)
  has_checked_out = models.BooleanField()

  def update_address(self, address):
    self.address = address
    self.save()



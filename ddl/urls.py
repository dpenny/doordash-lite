from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  url(r'^customers/(?P<customer_id>[0-9]+)/', CustomerDetailView.as_view()),
]
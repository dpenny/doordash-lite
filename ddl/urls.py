from django.conf.urls import url, include
from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  url(r'^customers/(?P<consumer_id>[0-9]+)/$', api.CustomerDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
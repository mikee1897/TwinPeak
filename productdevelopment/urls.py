from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add_a_customer/$', views.add_a_customer),
    url(r'^add_an_order/$', views.add_an_order),
]

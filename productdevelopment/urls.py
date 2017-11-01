from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^/add_customer$', views.add_customer),
	url(r'^add_order/$', views.add_order),
]
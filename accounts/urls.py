from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.authentication), #serve view depending on user && check if logged in or not
#	url(r'^login/$', views.login),
#	url(r'^logout/$', views.logout),
]
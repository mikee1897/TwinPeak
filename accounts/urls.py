from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.user_type_redirect), #serve view depending on user, authentication and redirect
									     #is done by middleware
	url(r'^login/$', views.log_in),
	url(r'^logout/$', views.log_out),
]
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.homepage_redirect), #serve view depending on user, authentication and redir 
									     #is done by middleware
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
]
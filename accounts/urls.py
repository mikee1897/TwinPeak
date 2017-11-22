from django.conf.urls import url, include
from . import views

urlpatterns = [
    # serve view depending on user, authentication and redirect
    url(r'^$', views.user_type_redirect),
    # is done by middleware
    url(r'^login/$', views.log_in),
    url(r'^logout/$', views.log_out),
]

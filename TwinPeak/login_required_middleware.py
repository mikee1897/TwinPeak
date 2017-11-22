from django.conf import settings
from django.shortcuts import redirect

import re

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
ADMIN_URLS = []
MATERIAL_PLANNING_URLS = []
PRODUCT_DEVELOPMENT_URLS = []
PRODUCTION_URLS = []

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

if hasattr(settings, 'ADMIN_URLS'):
	ADMIN_URLS += [re.compile(url) for url in settings.ADMIN_URLS]

if hasattr(settings, 'MATERIAL_PLANNING_URLS'):
	MATERIAL_PLANNING_URLS += [re.compile(url) for url in settings.MATERIAL_PLANNING_URLS]

if hasattr(settings, 'PRODUCT_DEVELOPMENT_URLS'):
	PRODUCT_DEVELOPMENT_URLS += [re.compile(url) for url in settings.PRODUCT_DEVELOPMENT_URLS]

if hasattr(settings, 'ADMIN_URLS'):
	PRODUCTION_URLS += [re.compile(url) for url in settings.PRODUCTION_URLS]	


class LoginRequiredMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		assert hasattr(request, 'user')
		path = request.path_info.lstrip('/')

		if not request.user.is_authenticated():
			print('is_authenticated - middleware part')
			if not any(url.match(path) for url in EXEMPT_URLS):
				return redirect(settings.LOGIN_URL)
		else:
			user_type = request.user.UserProfile.user_type
			if user_type == 'admin':
				if not any(url.match(path) for url in ADMIN_URLS):
					return redirect('/404') # TODO: 404 page
			elif user_type == 'materialplanning':
				if not any(url.match(path) for url in MATERIAL_PLANNING_URLS):
					return redirect('/404') 
			elif user_type == 'productdevelopment':
				if not any(url.match(path) for url in PRODUCT_DEVELOPMENT_URLS):
					return redirect('/404')
			elif user_type == 'production':
				if not any(url.match(path) for url in PRODUCTION_URLS):
					return redirect('/404')

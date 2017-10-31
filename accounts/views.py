from django.shortcuts import render, redirect
from django.contrib.auth import login

def homepage_redirect(request):
	user_type = request.user.userprofile.user_type
	if user_type == 'productdevelopment':
		pass
	elif user_type == 'materialplanning':
		pass
	elif user_type == 'production':
		pass
	elif user_type == 'admin':
		pass

def login(request):
	username = request.POST('username')
	password = request.POST('password')
	user = authenticate(request, username=username, password=password)
	user_type = user.userprofile.user_type
	if user is not None:
		login(request, user)
	else:
		pass

def logout(request):
	logout(request)
	return redirect('/')
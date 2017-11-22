from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

"""Redirect is handled by this view, to give users appropriate template.
Authentication redirect and users having invalid permission is done by
Twinpeak/TwinPeak/login_required_middleware.py
"""
def user_type_redirect(request):
	user_type = request.user.UserProfile.user_type
	if user_type == 'materialplanning':
		pass

def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print('success')
			return redirect('/') #goes to homepage_redirect
		else:
			args = {'login_error': 'true'}
			return render(request, 'login.html', args)
			print('error')
	else:
		return render(request, 'login.html')
		print('non user request')


def log_out(request):
	logout(request)
	return redirect('/') #middleware redirects to login

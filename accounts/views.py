from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def homepage_redirect(request):
	"""	user_type = request.user.user_profile.user_type
	if user_type == 'productdevelopment':
		pass
	elif user_type == 'materialplanning':
		pass
	elif user_type == 'production':
		pass
	elif user_type == 'admin':
		print('admin')
		pass"""
	return render(request, 'accounts/admin_page.html')

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
			return render(request, 'accounts/login.html', args)
			print('error')
	else:
		return render(request, 'accounts/login.html')
		print('non user request')


def log_out(request):
	logout(request)
	return redirect('/') #middleware redirects to login
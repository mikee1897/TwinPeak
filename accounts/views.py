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
	if request.method =='POST'
		username = request.POST('username')
		password = request.POST('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/') #goes to homepage_redirect
		else:
			args = {'login_error': 'true'}
			return render(render, 'accounts/login.html', args)
	else:
		return render(render, 'accounts/login.html')


def logout(request):
	logout(request)
	return redirect('/') #middleware redirects to login
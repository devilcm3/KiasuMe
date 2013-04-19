# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from member.models import Profile

def login(request):
	# print request
	print request.session.get('redirect_field_name')
	if 'username' in request.POST and 'password' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)

				success = "Login successful!"
				return render(request,'common/success.html',{"success":success})
			else:
				print "you've been banned! oops!"
		else:
			print "wrong password perhaps?"
	else:
		return render(request,'member/login.html')

@login_required
def logout(request):
	auth_logout(request)
	success = "Logout successful! See you again!"
	return render(request,'common/success.html',{"success":success})


def register(request):
	if request.method == 'POST':
		return render(request,'common/success.html')
	else:
		return render(request,'member/register.html')

# Create your views here.
import uuid
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import simplejson
from django.core.exceptions import PermissionDenied
from member.models import Profile, RegEmail
from member.forms import EditProfileForm, NewProfileForm, ChangePasswordForm, ResetPasswordForm
from deal.forms import GetDealForm
from store.models import Store
from deal.models import Deal, Subcategory
from member.utils import reset_password_mail

def reset_password(request):
	if request.method == 'POST':
		p = Profile.objects.filter(username = request.POST['username'], email= request.POST['email'])
		if p.exists():
			p = p[0]
			newpass = str(uuid.uuid4()).split('-')[0]
			p.set_password(newpass)
			p.save()
			reset_password_mail(email = p.email, username = p.username, password = newpass)

			success = "We have sent a new password to your email address, please check your email in a few minutes"
			return render(request,'common/success.html',{"success":success})
		else:
			error_message = 'No username with such email address found, try again?'
	form = ResetPasswordForm()
	return render(request,'member/reset_password.html',{'form':form, 'error_message':error_message})


def login(request):
	# print request
	message = ''
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
				message = "Have you activated your account yet?"
		else:
			message = "Login Failed, check username and password"
	return render(request,'member/login.html',{'message':message})

def register(request):
	if request.method == 'POST':
		form = NewProfileForm(data = request.POST)
		if form.is_valid():
			form.save()
			return render(request,'member/register_success.html')
	else:
		form = NewProfileForm()

	return render(request,'member/register.html',{'form':form})

def register_confirmation(request,code,rubbish):
	code = code.rsplit('-',1)
	reg_id = code[1]
	code = code[0]

	print code
	print reg_id
	try:
		reg = RegEmail.objects.get(id = reg_id)
		print reg
		if reg.verification == code:
			Profile.objects.filter(id = reg.profile_pk.id).update(is_active = True)
			return render(request,'member/register_email_confirm.html')
		else:
			raise PermissionDenied
	except:
		raise PermissionDenied

	return render(request,'member/register_email_confirm.html')


def public_profile(request,pid):
	try:
		context = {
		'profile': Profile.objects.get(id=pid),
		'menu_active': {'profile':'active'}
		}
		return render(request,'member/public_profile.html',context)
	except:
		return render(request,'member/public_profile_not_exists.html')

def public_profile_deals(request,pid):
	context = {
	'deals': Deal.objects.filter(member_pk=pid),
	'menu_active': {'deals':'active'},
	'profile':{'id':pid}
	}
	return render(request,'member/public_profile_deals.html',context)

@login_required
def logout(request):
	auth_logout(request)
	success = "Logout successful! See you again!"
	return render(request,'common/success.html',{"success":success})

@login_required
def cpanel_profile(request):
	context = {
	'profile': Profile.objects.get(id = request.user.id),
	'menu_active': {'profile':'active'}
	}
	return render(request,'member/cpanel/index.html',context)

@login_required
def cpanel_edit_profile(request):
	profile = Profile.objects.get(id = request.user.id)
	if request.method == 'POST':
		form = EditProfileForm(data = request.POST, instance = profile)
		if form.is_valid():
			form.save()
			return redirect('/member/cpanel/')
	else:
		form = EditProfileForm(instance = profile)
	return render(request,'member/cpanel/edit_profile.html',{'form':form})

@login_required
def cpanel_change_password(request):
	profile = Profile.objects.get(id = request.user.id)
	if request.method == 'POST':
		form = ChangePasswordForm(data = request.POST, instance = profile)
		if form.is_valid():
			form.save()
			return redirect('/member/cpanel/')
	else:
		form = ChangePasswordForm()
	return render(request,'member/cpanel/change_password.html',{'form':form})

@login_required
def cpanel_view_deals(request):	
	deals = Deal.objects.filter(member_pk=request.user.id)
	return render(request,'member/cpanel/deals.html',{'deals':deals})

@login_required
def cpanel_edit_deal(request,did):
	subcategories = simplejson.dumps([{'name':o.name,'id':o.id,'category':o.category_pk.id} for o in Subcategory.objects.all().select_related()])
	try:
		deal = Deal.objects.get(id=did, member_pk=request.user.id)
	except:
		raise PermissionDenied
	if request.method == 'POST':
		form = GetDealForm(data = request.POST, files = request.FILES, instance = deal, exclude_list = ('date_created','date_modified','active','total_vote','member_pk'))
		form = form()
		if form.is_valid():
			form.save()
			return redirect('/member/cpanel/deals/')
	else:
		form = GetDealForm(instance=deal, exclude_list=('date_created','date_modified'))
		form = form()

	return render(request,'member/cpanel/edit_deal.html',{ 'form':form, 'deal':deal, 'subcategories':subcategories})

@login_required
def cpanel_delete_deal(request,did):
	try:
		deal = Deal.objects.get(id=did, member_pk=request.user.id)
		deal.delete()
		return redirect('/member/cpanel/deals')
	except:
		raise PermissionDenied
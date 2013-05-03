# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from django.core import serializers
from django.utils import simplejson
from deal.models import *
from deal.forms import *
from datetime import date,time,datetime
from django.http import HttpResponse #,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# import os

def hot_deals(category_id = None):
	today = [
		datetime.combine(date.today(),time.min),
		datetime.combine(date.today(),time.max)
	]
	if category_id:
		return Deal.objects.filter(date_created__range=(today[0],today[1])).filter(category_pk=category_id, active=True, total_vote__gt = 0).values('id','title').order_by('-total_vote')[:5]
	else:
		return Deal.objects.filter(date_created__range=(today[0],today[1])).filter(active=True, total_vote__gt = 0).values('id','title').order_by('-total_vote')[:5]


def index(request, page_num = 1):
	pages = Paginator(Deal.objects.filter(active=True).order_by('-date_created').prefetch_related('category_pk','member_pk','subcategory_pk'), 10)
	if not page_num : page_num = 1

	context = {
	'deals' : pages.page(page_num),
	'hot_deals' : hot_deals(),
	'nav':'Home',
	'pagination_url':'/deal/'
	}
	return render(request,'common/layout.html',context)

def view(request,deal_id):
	try:
		deal = Deal.objects.select_related().get(id=deal_id)
		context = {
		'deal':deal,
		'hot_deals':hot_deals(deal.category_pk_id),
		'nav':deal.category_pk.name
		}
		return render(request,'deal/view.html',context)
	except:
		return render(request,'deal/not_exists.html')

def search(request, query):
	context = {
	'query':request.GET.get('q')
	}
	return render(request,'deal/search.html',context)

def category(request, category_id, category_name, subcategory_id = None, subcategory_name = None, page_num = 1):
	if subcategory_id and subcategory_name:
		pages = Paginator(Deal.objects.filter(subcategory_pk=subcategory_id).filter(active=True).order_by('-date_created'),10)
		pagination_url = '/deal/%s/%s/%s/%s/' %(category_id, category_name, subcategory_id, subcategory_name)
	else:
		pages = Paginator(Deal.objects.filter(category_pk=category_id).filter(active=True).order_by('-date_created'),10)
		pagination_url = '/deal/%s/%s/' %(category_id, category_name)

	if not page_num: page_num = 1
	context = {
	'deals':pages.page(page_num),
	'hot_deals':hot_deals(category_id),
	'nav':category_name,
	'pagination_url':pagination_url
	}
	return render(request,'common/layout.html',context)

def vote(request):
	if request.user.is_authenticated() and request.is_ajax():
		Deal.vote(request.POST['promo_id'], request.POST['promo_vote'])
		return HttpResponse(status = 200)
	else:
		return HttpResponse(status = 401)

@login_required
def create_new_deal(request):
	if request.method == 'POST':
		post_values = request.POST.copy()
		post_values['member_pk'] = request.user.id

		form = DealForm(post_values, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		subcategories = simplejson.dumps([{'name':o.name,'id':o.id,'category':o.category_pk.id} for o in Subcategory.objects.all().select_related()])
		exclude_list = ('active','promo_thumbnail','total_vote','member_pk','tag_pk')	
		form_class = GetDealForm(exclude_list)
		form = form_class()

	return render(request,'deal/new_deal.html',{'form':form,'subcategories':subcategories})

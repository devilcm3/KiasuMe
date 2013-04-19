# Create your views here.
# Create your views here.
from django.shortcuts import render #,redirect
from django.core import serializers
from promotion.models import *
from promotion.forms import *
from datetime import date,time,datetime
from django.http import HttpResponse #,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# import os

def hot_promotions(category_id = None):
	today = [
		datetime.combine(date.today(),time.min),
		datetime.combine(date.today(),time.max)
	]
	if category_id:
		return Promotion.objects.filter(date_created__range=(today[0],today[1])).filter(category_pk=category_id).filter(active=True).filter(total_vote__gt = 0).order_by('-total_vote')[:5]
	else:
		return Promotion.objects.filter(date_created__range=(today[0],today[1])).filter(active=True).filter(total_vote__gt = 0).order_by('-total_vote')[:5]


def index(request, page_num = 1):
	pages = Paginator(Promotion.objects.filter(active=True).order_by('-date_created'), 10)
	if not page_num : page_num = 1

	context = {
	'promotions' : pages.page(page_num),
	'hot_promotions' : hot_promotions(),
	'nav':'Home',
	'pagination_url':'/promotion/'
	}
	return render(request,'common/layout.html',context)

def view(request,promotion_id):
	promotion = Promotion.objects.get(id=promotion_id)
	context = {
	'promotion':promotion,
	'hot_promotions':hot_promotions(category_id),
	'nav':promotion.category_pk.name
	}
	return render(request,'promotion/view.html',context)

def search(request, query):
	context = {
	'query':request.GET.get('q')
	}
	return render(request,'promotion/search.html',context)

def category(request, category_id, category_name, subcategory_id = None, subcategory_name = None, page_num = 1):
	if subcategory_id and subcategory_name:
		pages = Paginator(Promotion.objects.filter(subcategory_pk=subcategory_id).filter(active=True).order_by('-date_created'),10)
		pagination_url = '/promotion/%s/%s/%s/%s/' %(category_id, category_name, subcategory_id, subcategory_name)
	else:
		pages = Paginator(Promotion.objects.filter(category_pk=category_id).filter(active=True).order_by('-date_created'),10)
		pagination_url = '/promotion/%s/%s/' %(category_id, category_name)

	if not page_num: page_num = 1
	context = {
	'promotions':pages.page(page_num),
	'hot_promotions':hot_promotions(),
	'nav':category_name,
	'pagination_url':pagination_url
	}
	return render(request,'common/layout.html',context)

def vote(request):
	if request.is_ajax():
		Promotion.vote(request.POST['promo_id'], request.POST['promo_vote'])
		return HttpResponse('ok',mimetype='application/json')

@login_required
def create_new_promotion(request):
	if request.method == 'POST':
		post_values = request.POST.copy()
		post_values['member_pk'] = request.user.id

		form = PromotionForm(post_values, request.FILES)
		if form.is_valid():
			form.save()
			print 'everything done!'
	else:
		exclude_list = ('active','promo_thumbnail','total_vote','member_pk','tag_pk')	
		form_class = GetUserPromotionForm(exclude_list)
		form = form_class()

	return render(request,'promotion/new_promotion.html',{'form':form})

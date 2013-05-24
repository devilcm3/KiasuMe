from django.conf.urls import patterns,url,include
from deal import views
from deal.feeds import LatestEntriesFeed

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^search/(?P<query>.*)/?$', views.search, name='search'),
	url(r'^(?P<page_num>\d*)/$',views.index, name='index'),
	url(r'^vote/$',views.vote, name='vote'),
	url(r'^new/$',views.create_new_deal, name='new_deal'),
	url(r'^view/(?P<deal_id>\d+)/.{0,250}/?$',views.view, name='view'),
	url(r'^(?P<category_id>\d+)/(?P<category_name>[\w\&\-\s]+)/(?P<page_num>\d*)/?$',views.category, name='category_with_name'),
	url(r'^(?P<category_id>\d+)/(?P<category_name>[\w\&\-\s]+)/(?P<subcategory_id>\d+)/(?P<subcategory_name>[\w\&\-\s]+)/(?P<page_num>\d*)/?$',views.category, name='subcategory_with_name'),
	url(r'^feeds/', LatestEntriesFeed())
)
from django.conf.urls import patterns,url,include
from member import views

urlpatterns = patterns('',
	url(r'^(?P<pid>\d+)/$', views.public_profile),
	url(r'^(?P<pid>\d+)/deals/$', views.public_profile_deals),
	url(r'^confirm/(?P<code>[\-\w]{10,100})/(?P<rubbish>[\-\w]{10,100})/$', views.register_confirmation),
	url(r'^reset_password/$', views.reset_password),
	url(r'^cpanel/$', views.cpanel_profile),
	url(r'^cpanel/change_password$', views.cpanel_change_password),
	url(r'^cpanel/edit$', views.cpanel_edit_profile),
	url(r'^cpanel/deals/$', views.cpanel_view_deals),
	url(r'^cpanel/deals/edit/(?P<did>\d+)/$', views.cpanel_edit_deal),
	url(r'^cpanel/deals/delete/(?P<did>\d+)/$', views.cpanel_delete_deal),
)
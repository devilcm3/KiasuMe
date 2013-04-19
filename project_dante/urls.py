from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^register/$','member.views.register',name="register"),
    url(r'^login/$','member.views.login',name="login"),
    url(r'^logout/$','member.views.logout',name="logout"),

    url(r'',include('social_auth.urls')),

    url(r'^$','promotion.views.index',name="home"),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^manage/',include(admin.site.urls)),
    url(r'^promotion/',include('promotion.urls',namespace="promotion")),
    # url(r'^$', 'project_dante.views.home', name='home'),
    # url(r'^project_dante/', include('project_dante.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$','django.views.static.serve',{
		'document_root':settings.MEDIA_ROOT
		}
	))
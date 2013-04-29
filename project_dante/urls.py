from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from deal.sitemaps import DealSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()

admin.autodiscover()

sitemaps = {
    'deal': DealSitemap
}

urlpatterns = patterns('',
    # Examples:
    url(r'^register/$','member.views.register',name="register"),
    url(r'^login/$','member.views.login',name="login"),
    url(r'^logout/$','member.views.logout',name="logout"),
    url(r'',include('social_auth.urls')),
    url(r'^$','deal.views.index',name="home"),
    url(r'^deal/',include('deal.urls',namespace="deal")),
    url(r'^member/',include('member.urls',namespace="member")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^manage/',include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

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
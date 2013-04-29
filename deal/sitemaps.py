from django.contrib.sitemaps import Sitemap
from deal.models import Deal

class DealSitemap(Sitemap):
	changefreq = 'never'
	priority = 0.5

	def items(self):
		return Deal.objects.filter(active = True).only('id','slug','date_modified')

	def location(self, obj):
		return str('/deal/view/'+str(obj.id)+'/'+obj.slug)

	def lastmod(self, obj):
		return obj.date_modified


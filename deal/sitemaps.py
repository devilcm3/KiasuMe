from django.contrib.sitemaps import Sitemap
from deal.models import Deal, Category, Subcategory

class DealSitemap(Sitemap):
	changefreq = 'never'
	priority = 0.5

	def items(self):
		return Deal.objects.filter(active = True).only('id','slug','date_modified')

	def location(self, obj):
		return str('/deal/view/'+str(obj.id)+'/'+obj.slug)

	def lastmod(self, obj):
		return obj.date_modified

class DealCategorySitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5

	def items(self):
		return Category.objects.all()

	def location(self, obj):
		return str('/deal/'+str(obj.id)+'/'+str(obj.name))

class DealSubcategorySitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5

	def items(self):
		return Subcategory.objects.all().select_related()

	def location(self, obj):
		return str('/deal/'+str(obj.category_pk.id)+'/'+str(obj.category_pk.name)+'/'+str(obj.id)+'/'+str(obj.name))
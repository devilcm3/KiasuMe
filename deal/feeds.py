from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from deal.models import Deal

class LatestEntriesFeed(Feed):
	title = "Kiasu ME latest deals"
	link = "/deal/feeds/"
	description = "Everything about latest deals in KiasuME"

	def items(self):
		return Deal.objects.order_by('-date_created')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content

	def item_link(self, item):
		abs_url = "http://kiasu.me/deal/view" + str(item.id) + "/" + item.slug
		return abs_url
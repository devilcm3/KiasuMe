from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	can_import_settings = True

	def handle(self, *args, **kwargs):
		from deal.models import *
		from datetime import date, datetime, timedelta
		from project_dante import settings
		from open_facebook.api import OpenFacebook
		from django.core.files.base import ContentFile
		from django.core.paginator import Paginator
		import re, urllib2

		graph 			= OpenFacebook(settings.FACEBOOK_APP_ID + '|' + settings.FACEBOOK_APP_SECRET)
		facebook_pages 	= Paginator(FacebookFeed.objects.all(),20)
		page_num 		= 1


		while page_num <= facebook_pages.num_pages:
			queries 		= {}
			current_page 	= facebook_pages.page(page_num)
			for p in current_page:
				query 	= "SELECT post_id, attachment, message FROM stream WHERE source_id = %s and type = 247" % (p.page_id)
				queries[unicode('p_'+p.page_id)] = query

			query_result = graph.batch_fql(queries)
			keyword = r'\b(hot|deal|sale|promotion|off|free|[\d]{1,3}%{1})+'

			for p in current_page:
				if query_result[unicode('p_'+p.page_id)]:
					result = query_result[unicode('p_'+p.page_id)]
					for data in result:
						if (data['post_id'] != p.recent_feed) and (p.recent_feed != ''):
							if (re.search(keyword,data['message'],flags=re.I)):
								media 				= data['attachment']['media'][0]
								deal 				= Deal()
								deal.title 			= "%s : %s ..." % (p.page_name[:25], data['message'][:115]) 
								deal.link 			= media['href']
								deal.content 		= '<p>' + data['message'].replace('\n','<br>') + '</p>'
								deal.date_started	= date.today()
								image_content 		= ContentFile(urllib2.urlopen(media['src'].replace('_s.','_n.')).read())
								deal.promo_image.save(media['src'].split('/')[-1].replace('_s.','_n.'), image_content, save=False)
								deal.category_pk	= p.category_pk
								deal.member_pk		= p.member_pk
								deal.save()
						else:
							break
					p.recent_feed = result[0]['post_id'] #updates entry to the most recent feed
					p.save()

			print "page num : %s" %(page_num)
			page_num+=1
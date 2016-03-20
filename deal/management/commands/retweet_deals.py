from django.core.management.base import BaseCommand, CommandError
from twitter import *

class Command(BaseCommand):
	can_import_settings = True

	def handle(self, *args, **options):
		from datetime import date, datetime, timedelta
		now = datetime.now()
		hourmin = now.replace(hour=3,minute=0,second=0,microsecond=0)
		hourmax = now.replace(hour=8,minute=0,second=0,microsecond=0)

		if not (hourmin < now < hourmax):
			from random import randint
			from django.db.models import Q				
			from deal.models import Deal
			from project_dante import settings

			foodmin_1 = now.replace(hour=10,minute=0,second=0,microsecond=0)
			foodmax_1 = now.replace(hour=14,minute=0,second=0,microsecond=0)

			foodmin_2 = now.replace(hour=17,minute=0,second=0,microsecond=0)
			foodmax_2 = now.replace(hour=20,minute=0,second=0,microsecond=0)

			t = Twitter(auth = OAuth(settings.KIASU_OAUTH_TOKEN, settings.KIASU_OAUTH_SECRET, settings.KIASU_CONSUMER_KEY, settings.KIASU_CONSUMER_SECRET))

			if ((foodmin_1 < now < foodmax_1) or (foodmin_2 < now < foodmax_2)):
				deals = Deal.objects.filter( Q(date_ended__isnull=True)|Q(date_ended__gte=date.today()) , Q(date_created__gte=(date.today()-timedelta(14))), Q(category_pk='1') ).order_by('?').select_related()[:3]
				for deal in deals:
					try:
						status_msg = "FOODIE HOUR : "+deal.title[:75]+"... #deal kiasu.me/dv/" + str(deal.id) + "/" + str(randint(1,100))
						t.statuses.update(status = status_msg)
					except:
						pass
			else:
				deals = Deal.objects.filter( Q(date_ended__isnull=True)|Q(date_ended__gte=date.today()) , Q(date_created__gte=(date.today()-timedelta(7))) ).order_by('?').select_related()[:3]
				for deal in deals:
					try:
						status_msg = deal.member_pk.username[:15]+" posted: "+deal.title[:75]+"... #deal kiasu.me/dv/" + str(deal.id) + "/" + str(randint(1,100))
						t.statuses.update(status = status_msg)
					except:
						pass
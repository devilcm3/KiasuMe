from django.core.management.base import BaseCommand, CommandError
from twitter import *

class Command(BaseCommand):
	can_import_settings = True

	def handle(self, *args, **options):
		from datetime import date, datetime, timedelta
		now = datetime.now()
		hourmin = now.replace(hour=3,minute=0,second=0,microsecond=0)
		hourmax = now.replace(hour=9,minute=0,second=0,microsecond=0)

		if not (hourmin < now < hourmax):
			from random import randint
			from django.db.models import Q				
			from deal.models import Deal
			from project_dante import settings

			t = Twitter(auth = OAuth(settings.KIASU_OAUTH_TOKEN, settings.KIASU_OAUTH_SECRET, settings.KIASU_CONSUMER_KEY, settings.KIASU_CONSUMER_SECRET))
			deals = Deal.objects.filter( Q(date_ended__isnull=True)|Q(date_ended__gte=date.today()) , Q(date_created__gte=(date.today()-timedelta(3))) ).order_by('?').select_related()[:1]
			for deal in deals:
				try:
					status_msg = deal.member_pk.username[:15]+" posted: "+deal.title[:75]+"... #fb #discount kiasu.me/dv/" + str(deal.id) + "/" + str(randint(1,100))
					t.statuses.update(status = status_msg)
				except:
					pass
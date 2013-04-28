from django import template
from deal.models import Category
register = template.Library()

@register.inclusion_tag('common/navigation_menu.html')
def show_navigation_menu(**kwargs):
	kwargs[kwargs.get('active')] = 'active'
	# links = [{'name':'Home','url':'/',kwargs.get('Home',"-"):'active'}]
	links = []
	for cat in Category.objects.all().order_by('priority'):
		links.append({'name':cat.name, 'id':cat.id, 'subcats':cat.subcategory_set.all(), kwargs.get(cat.name,"-"):'active'})
	return {'links':links}
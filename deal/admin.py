from django.contrib import admin
from django import forms
from deal.models import *
from deal.forms import *
from project_dante import settings
class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)

class DealRatingAdmin(admin.ModelAdmin):
	list_display = ('vote','deal_pk','member_pk')
	
class DealAdmin(admin.ModelAdmin):
	form = DealForm

	list_display = ('id','title','member_pk','active','total_vote','date_created','date_modified','date_started','date_ended','promo_image','promo_thumbnail','slug')
	fieldsets = (
		('Main Information',{'fields' : ('title','content') }),
		('Category',{'fields':('category_pk','subcategory_pk')}),
		('Dates',{'fields': ('date_started','date_ended') }),
		('Files',{'fields': ('promo_image','promo_file') }),
		('Tags',{'fields': ('tag_pk',)})
	)

	add_fieldsets = (
		('Main Information',{'fields' : ('title','content') }),
		('Category',{'fields':('category_pk','subcategory_pk')}),
		('Dates',{'fields': ('date_started','date_ended') }),
		('Files',{'fields': ('promo_image','promo_file') }),
		('Tags',{'fields': ('tag_pk',)})
	)

	def save_model(self, request, obj, form, change):
		obj.member_pk = request.user
		obj.save()

	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			settings.STATIC_URL + 'ckeditor/ckeditor.js',
			settings.STATIC_URL + 'js/admin/custom_admin.js'
		)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','priority')

class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('name','priority')

admin.site.register(Tag, TagAdmin)
admin.site.register(DealRating, DealRatingAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
from django.contrib import admin
from django import forms
from promotion.models import *
from promotion.forms import *
class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)

class PromotionRatingAdmin(admin.ModelAdmin):
	list_display = ('vote','promotion_pk','member_pk')
	
class PromotionAdmin(admin.ModelAdmin):
	form = PromotionForm

	list_display = ('title','active','total_vote','date_created','date_modified','date_started','date_ended','promo_image','promo_thumbnail')
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

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','priority')

class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('name','priority')

admin.site.register(Tag, TagAdmin)
admin.site.register(PromotionRating, PromotionRatingAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
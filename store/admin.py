from django.contrib import admin
from django import forms
from store.models import *

class ProvinceAdmin(admin.ModelAdmin):
	list_display = ('name',)

class AreaAdmin(admin.ModelAdmin):
	list_display = ('province_pk','name')

class StoreAdmin(admin.ModelAdmin):
	list_display = ('name','address','province_pk','area_pk','postcode','phone_1','phone_2','fax','total_vote','member_pk')

admin.site.register(Province,ProvinceAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Store,StoreAdmin)
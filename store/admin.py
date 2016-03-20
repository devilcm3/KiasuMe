from django.contrib import admin
from django import forms
from store.models import *

class AreaAdmin(admin.ModelAdmin):
	list_display = ('name',)

class StoreAdmin(admin.ModelAdmin):
	list_display = ('name','address','area_pk','postcode','landline_1','landline_2','fax','mobile','website','email','total_vote','member_pk')

admin.site.register(Area,AreaAdmin)
admin.site.register(Store,StoreAdmin)
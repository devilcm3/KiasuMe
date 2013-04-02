from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from member.models import Profile

class ProfileCreationForm(forms.ModelForm):
	class Meta:
		model = Profile

class ProfileChangeForm(forms.ModelForm):
	class Meta:
		model = Profile

class ProfileAdmin(UserAdmin):
	#CANNOT BE THE SAME AS CLASSNAME USERCHANGEFORM, CLASH
	form = ProfileChangeForm
	add_form = ProfileCreationForm

	list_display = ('id','username','email','full_name','phone_1','is_staff',)
	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal Info'), {'fields': ('full_name','address')}),
        (('Contact'), {'fields': ('phone_1','phone_2','fax','email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
	add_fieldsets = ((None,{'fields':('username','password')}),
		('Personal Info',{'fields':('full_name','address',)}),
		(('Contact'), {'fields': ('phone_1','phone_2','fax','email')}),
	)


admin.site.unregister(Group)
admin.site.register(Profile,ProfileAdmin)
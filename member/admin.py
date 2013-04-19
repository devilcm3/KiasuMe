from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from member.models import Profile

class ProfileCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
		model = Profile

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match	')
        return password2

    def save(self, commit=True):
        user = super(ProfileCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()
	class Meta:
		model = Profile

class ProfileAdmin(UserAdmin):
	#CANNOT BE THE SAME AS CLASSNAME USERCHANGEFORM, CLASH
	form = ProfileChangeForm
	add_form = ProfileCreationForm
	list_display = ('id','username','email','first_name','last_name','phone_1','is_staff',)
	fieldsets = (
        (None, {'fields': ('username',)}),
        (('Personal Info'), {'fields': ('first_name','middle_name','last_name','address')}),
        (('Contact'), {'fields': ('phone_1','phone_2','fax','email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
	add_fieldsets = ((None,{'fields':('username','password1','password2')}),
		('Personal Info',{'fields':('first_name','middle_name','last_name','address',)}),
		(('Contact'), {'fields': ('phone_1','phone_2','fax','email')}),
	)

admin.site.register(Profile,ProfileAdmin)
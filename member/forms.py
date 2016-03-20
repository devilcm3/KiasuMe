from django import forms
from member.models import Profile,RegEmail

class ProfileForm(forms.ModelForm):
	password = forms.CharField(label= u'Password', widget = forms.PasswordInput(), required=True)
	password2 = forms.CharField(label= u'Password (Again)', widget = forms.PasswordInput(), required=True)

	def clean(self):
		cleaned_data = super(ProfileForm,self).clean()
		if('password' not in cleaned_data or 'password2' not in cleaned_data):
			raise forms.ValidationError('Error, please check input boxes again')
		else:
			if(cleaned_data['password'] != cleaned_data['password2']):
				raise forms.ValidationError('Passwords do not match')
			return self.cleaned_data

	def save(self, commit=True):
		profile = super(ProfileForm, self).save(commit=False)
		profile.set_password(self.cleaned_data['password'])
		if commit:
			profile.save()
		return profile	

	class Meta:
		model = Profile

class NewProfileForm(ProfileForm):
	email = forms.EmailField(required=True)

	def clean(self):
		cleaned_data = super(NewProfileForm,self).clean()
		if ('email' not in cleaned_data):
			raise forms.ValidationError('Email is required')
		elif (Profile.objects.filter(email__exact=cleaned_data['email']).count()):
			raise forms.ValidationError('This email has already been registered')
		return self.cleaned_data

	def save(self, commit=True):
		profile = super(NewProfileForm, self).save(commit=False)
		profile.is_active = False
		if commit:
			profile.save()
			reg = RegEmail(profile_pk = profile)
			reg.save()
		return profile

	class Meta:
		fields = ('username','password','password2','email')
		model  = Profile

class EditProfileForm(forms.ModelForm):
	class Meta:
		fields = ('first_name','middle_name','last_name','email','website','address','landline_1','landline_2','fax','mobile')
		model 	= Profile

class ChangePasswordForm(ProfileForm):
	class Meta:
		fields = ('password','password2')
		model = Profile

class ResetPasswordForm(forms.ModelForm):
	class Meta:
		fields = ('username','email')
		model = Profile
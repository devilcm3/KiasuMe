from django import forms
from datetime import date
from promotion.models import Promotion

class PromotionForm(forms.ModelForm):
	def clean(self):
		cleaned_data = super(PromotionForm, self).clean()
		date_started = cleaned_data['date_started']
		date_ended 	 = cleaned_data['date_ended']
		promo_image	 = cleaned_data['promo_image']
		promo_file	 = cleaned_data['promo_file']

		cleaned_data['total_vote'] = 0
		cleaned_data['active'] = 1


		if('content' in cleaned_data):
			cleaned_data['content'] = cleaned_data['content'].replace('script','')

		if(date_ended < date_started):
			raise forms.ValidationError("DATE ENDED cannot be earlier than DATE STARTED")
		elif(date_started < date.today()):
			raise forms.ValidationError("DATE STARTED and DATE ENDED starting from today onwards")
			
		if(promo_image):
			if (promo_image.size > 2097152):
				raise forms.ValidationError("Image size should be lower than 2 MegaBytes")
		if(promo_file):
			if(promo_file.size > 2097152):
				raise forms.ValidationError("File size should be lower than 2 MegaBytes")

		return self.cleaned_data

	class Meta:
		model = Promotion


def GetUserPromotionForm(exclude_list, *args, **kwargs):
	class UserPromotionForm(PromotionForm):
		class Meta:
			model = Promotion
			exclude = exclude_list

		def __init__(self):
			super(PromotionForm,self).__init__(*args,**kwargs)

	return UserPromotionForm

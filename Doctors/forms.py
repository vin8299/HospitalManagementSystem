from django import forms
from .models import Doctor
from django.core.files.images import get_image_dimensions

class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		def clean_image(self,*args,**kwargs):
			image = self.cleaned_data.get("image")
			if not image:
				raise forms.ValidationError("Image required")
			else:
				width, height = get_image_dimensions(image)
				if width>100 and heiht>200:
					raise forms.ValidationError("Image dimension should be less than 100*200")

			return image
		fields = [
					"d_name",
					"image",
					"d_address",
					"contact_no",
					"speciality",
				 ]



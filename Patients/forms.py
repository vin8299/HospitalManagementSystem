from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
					"p_name",
					"p_age",
					"p_sex",
					"p_address",
					"disease",
					"contact_no",
					"ward_no"
				 ]
